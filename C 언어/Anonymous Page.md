## Anonymous Page

이 프로젝트의 이 부분에서는 익명 페이지라는 비디스크 기반 이미지를 구현합니다.

익명 매핑에는 백업 파일이나 장치가 없습니다. 파일 기반 페이지와 달리 명명된 파일 소스가 없기 때문에 익명입니다. 익명 페이지는 스택 및 힙과 같은 실행 파일에서 사용됩니다.

`anon_page` 익명 페이지 인을 설명하는 구조체가 있습니다. `include/vm/anon.h` . 현재는 비어있지만 구현하면서 필요한 정보나 익명 페이지의 상태를 저장하기 위해 멤버를 추가할 수 있습니다. 또한 페이지의 일반 정보를 포함하는 `struct page` 를 참조하십시오. `include/vm/page.h`  익명 페이지의 경우 `struct anon_page anon`  해당 페이지 구조에 포함됩니다.



### Page Initialization with Lazy Loading

레이지 로딩은 필요한 시점까지 메모리 로딩을 연기하는 디자인입니다. 페이지가 할당되면 해당 페이지에 해당하는 페이지 구조체가 할당되지만, 전용 물리 프레임은 없으며 실제 페이지 내용은 아직 로드되지 않습니다. 페이지 내용은 페이지 폴트에 의해 실제 필요한 시점에만 로드 됩니다.

세가지 페이지 유형이 있으므로, 초기화 루틴은 각 페이지 유형마다 다릅니다. 아래 섹션에서 다시 설명하겠지만,  여기에서는 페이지 초기화 흐름의 고수준 개요를 제공합니다, 

1. 먼저 커널이 새 페이지 요청을 받으면 `vm_alloc_page_with_initializer()` 가 호출됩니다. 이니셜 라이저는 페이지 유형에 따라 적절한 이니셜 라이저를 설정하고 페이지 구조체를 할당하여 새 페이지를 초기화하고 사용자 프로그램에게 제어를 반환합니다.
2.  사용자 프로그램이 실행되는 동안, 어느 지점에서는 프로그램이 해당 페이지를 보유하고 있으며 해당 페이지에 액세스하려고 시도하여 페이지 폴트가 발생합니다.
3. 폴트 처리 절차 중에 uninit_initialize이 호출되고, 이전에 설정한 이니셜라이저를 호출합니다. 익명 페이지의 경우 anon_initializer를 사용하고, 파일 지원 페이지의 경우 file_backed_initializer를 사용합니다.

 

페이지는 초기화 -> (페이지 폴트->레이지 로드-> 스왑 인 -> 스왑 아웃 ->.....) -> 소멸의 수명 주기를 가질 수 있습니다. 수명주기의 각 전이마다 페이지 유형(또는 VM_TYPE)에 따라 필요한 절차가 다르며, 이전 단락은 초기화에 대한 예제 였습니다. 이 프로젝트에서는 각 페이지 유형에 대한 이러한 전이 프로세스를 구현하게 됩니다. 



#### Lazy Loading for Executable

레이지 로딩에서는 프로세스가 실행될 때 즉시 필요한 메모리 부분만 메인 메모리로 로드 됩니다. 이는 eager loading과 비교하여 모든 바이너리 이미지를 한 번에 메모리로 로드하는 것에 비해 오버헤드를 줄일 수 있습니다.

레이지 로딩을 지원하기 위해 `include/vm/vm.h` 에 `VM_UNINIT` 이라는 페이지 타입을 도입합니다. 모든 페이지는 처음에 `VM_UNINIT` 페이지로 생성됩니다. 또한 초기화되지 않은 페이지에 대한 페이지 구조체(`struct uninit_page`)를 제공합니다. 초기화 되지 않은 페이지를 생성, 초기화 및 소멸하는 함수는 `include/vm/uninit.c` 에서 찾을 수 있습니다. 

페이지 폴트가 발생하면(`page_fault in userprog/exception.c`), 페이지 폴트 핸들러는 `vm/vm.c` 의 `vm_try_handle_fault` 로 제어를 전달합니다. 이 함수에서는 먼저 유효한 페이지 폴트인지 확인합니다. 여기서 유효하다는 것은 유효하지 않은 메모리에 접근하는 폴트를 의미합니다. 만약 폴트가 잘못된 경우, 페이지에 일부 내용을 로드하고 사용자 프로그램으로 제어를 반환합니다.

잘못된 페이지 폴트의 경우 세가지 경우가 있습니다. 레이지 로드된 페이지, 스왑아웃된 페이지 및 쓰기 보호된 페이지 지금은 첫 번째 경우인 레이지 로드된 페이지만 고려합니다. 만약 레이지 로딩을 위한 페이지 폴트인 경우, 커널은 `vm_alloc_page_with_initializer`에서 이전에 설정한 초기화 함수 중 하나를 호출하여 세그먼트를 레이지 로드합니다. `userprog/process.c` 에서 `lazy_load_segment`를 구현해야 합니다.

`vm_alloc_page_with_initializer()`를 구현하세요. 전달된 `vm_type`에 따라 적절한 초기화 함수를 가져와 `uninit_new`를 호출해야 합니다.

```c
bool vm_alloc_page_with_initializer (enum vm_type type, void *va,
        bool writable, vm_initializer *init, void *aux);
```

> 주어진 타입으로 초기화되지 않은 페이지를 생성합니다. 초기화되지 않은 페이지의 swap_in 핸들러는 타입에 따라 자동으로 페이지를 초기화하고 주어진 AUX와 함께 INIT을 호출합니다. 페이지 구조체를 얻은 후, 프로세스의 보조 페이지 테이블에 페이지를 삽입합니다. `vm.h`에 정의된 `VM_TYPE` 매크로를 사용하는 것이 편리합니다.



페이지 폴트 핸들러는 호출 체인을 따라 `uninit_initialize`을 호출할 때 `swap_in`에 도달합니다. 이것의 완전한 구현을 제공합니다. 그러나 당신의 설계에 따라 `uninit_initialize`을 수정해야 할 수도 있습니다.



```c
static bool uninit_initialize (struct page *page, void *kva);
```

> 첫 번째 폴트 시 페이지를 초기화합니다. 템플릿 코드는 먼저 `vm_initializer`와 `aux`를 가져와 함수 포인터를 통해 해당 페이지 이니셜라이저를 호출합니다. 설계에 따라 함수를 수정해야 할 수도 있습니다.



```c
void vm_anon_init (void);
```

> 익명 페이지 하위 시스템을 위한 초기화 함수입니다. 이 함수에서는 익명 페이지와 관련된 모든 것을 설정할 수 있습니다.



```c
bool anon_initializer (struct page *page,enum vm_type type, void *kva);
```

> 이 함수는 페이지->operations에서 익명 페이지를 위한 핸들러를 설정합니다. 현재 빈 구조체인 anon_page에서 일부 정보를 업데이트해야 할 수도 있습니다. 이 함수는 익명 페이지 (즉, VM_ANON)의 초기화기로 사용됩니다.


`userprog/process.c`에 있는 `load_segment`와 `lazy_load_segment` 함수를 구현해주세요. 실행 파일로부터 세그먼트를 로드하는 기능을 구현해야 합니다. 이들 페이지는 모두 게으르게 로드되어야 하며, 커널이 이들 페이지의 페이지 폴트를 가로채기 전까지는 메모리에 로드되지 않아야 합니다.

당신은 `load_segment`의 루프 안에서 `vm_alloc_page_with_initializer`를 호출하여 보류 중인 페이지 객체를 생성해야 합니다. 페이지 폴트가 발생하면 이 때 세그먼트가 실제 파일에서 로드됩니다.



```c
static bool load_segment (struct file *file, off_t ofs, uint8_t *upage,
        uint32_t read_bytes, uint32_t zero_bytes, bool writable);
```

> 현재 코드는 메인 루프 내에서 파일에서 읽어들일 바이트 수와 0으로 채울 바이트 수를 계산하고, `vm_alloc_page_with_initializer`를 호출하여 대기 중인 객체를 만듭니다. 당신은 `aux` 인자로 제공할 보조 값을 설정해야합니다. 바이너리 로딩에 필요한 정보를 포함하는 구조체를 만들어야 할 수도 있습니다.



```c
static bool lazy_load_segment (struct page *page, void *aux);
```

> `load_segment` 함수에서 `vm_alloc_page_with_initializer`의 네 번째 인자로 `lazy_load_segment` 함수가 전달되는 것을 볼 수 있습니다. 이 함수는 실행 파일 페이지의 초기화를 담당하며 페이지 폴트가 발생할 때 호출됩니다. 이 함수는 페이지 구조체와 `aux`를 인자로 받습니다. `aux`는 `load_segment`에서 설정한 정보입니다. 이 정보를 사용하여 세그먼트를 읽어들일 파일을 찾고, 해당 세그먼트를 메모리에 읽어들여야 합니다.



userprog/process.c 파일의 setup_stack 함수를 조정하여 새로운 메모리 관리 시스템에 스택 할당을 맞추어야 합니다. 첫 번째 스택 페이지는 느리게 할당할 필요가 없습니다. 명령 형 인수와 함께 로드 시 할당 및 초기화할 수 있으며, 이를 위해 대기할 필요가 없습니다. 스택을 식별하는 방법을 제공해야 할 수 있습니다. vm/vm.h의 vm_type에서 auxillary markers (예: VM_MARKER_0)를 사용하여 페이지를 표시할 수 있습니다.

마지막으로, vm_try_handle_fault 함수를 수정하여 추가 페이지 테이블을 확인하여 잘못된 주소에 해당하는 페이지 구조체를 해결합니다. 이를 위해서는 spt_find_page를 통해 보충 페이지 테이블을 확인해야 합니다.

모든 요구 사항을 구현 한 후에는 fork를 제외한 프로젝트 2의 모든 테스트가 통과해야합니다.



#### Supplemental Page Table - Revisit

이제 우리는 복사 및 정리 작업을 지원하기 위해 보충 페이지 테이블 인터페이스를 다시 살펴보겠습니다. 이러한 작업은 프로세스를 생성하거나(더 구체적으로 자식 프로세스를 생성하는) 제거할 때 필요합니다. 자세한 내용은 아래에 설명되어 있습니다. 보충 페이지 테이블을 다시 방문하는 이유는 이전에 구현한 초기화 함수 중 일부를 사용하고자 할 수 있기 때문입니다.

```c
bool supplemental_page_table_copy (struct supplemental_page_table *dst,
    struct supplemental_page_table *src);
```

> 부모 프로세스의 실행 컨텍스트를 상속해야 할 때(즉, fork() 호출시) 사용되는 dst로부터 src의 보조 페이지 테이블을 복사합니다. src의 보조 페이지 테이블의 각 페이지를 반복하고 dst의 보조 페이지 테이블의 해당 항목을 정확히 복사합니다. 초기화되지 않은 페이지를 할당하고 즉시 그들을 차지해야합니다.



```c
void supplemental_page_table_kill (struct supplemental_page_table *spt);
```

> 보충 페이지 테이블이 보유한 모든 자원을 해제합니다. 이 함수는 프로세스가 종료될 때 (`userprog/process.c`의 `process_exit()` 함수에서) 호출됩니다. 페이지 항목을 반복하고 테이블의 페이지에 대해 `destroy(page)`를 호출해야 합니다. 이 함수에서는 실제 페이지 테이블(pml4)과 물리적 메모리(palloc으로 할당된 메모리)에 대해 걱정할 필요가 없습니다. 이러한 자원은 보충 페이지 테이블이 정리된 후에 호출자가 정리합니다.



#### Page Cleanup

uninit_destroy 함수와 anon_destroy 함수를 vm/uninit.c와 vm/anon.c에 구현하세요. 이것은 초기화되지 않은 페이지에 대한 파괴 작업의 핸들러입니다. 초기화되지 않은 페이지는 다른 페이지 객체로 변환되지만, 프로세스가 종료될 때 여전히 uninit 페이지가 있을 수 있습니다.

```c
static void uninit_destroy (struct page *page);
```

> page_destroy 함수는 page 구조체가 가지고 있는 자원을 해제하는 함수입니다. 이 함수를 사용할 때는, 페이지의 vm_type을 체크하고 그에 맞는 처리를 해주어야 합니다. 예를 들어, vm_type이 VM_UNINIT인 경우에는 uninit_destroy를 호출하고, vm_type이 VM_ANON인 경우에는 anon_destroy를 호출해주어야 합니다. 만약 vm_type이 VM_FILE인 경우에는 파일에 대한 정보를 가지고 있는 file 구조체를 해제해주어야 합니다. 이러한 처리들을 해주고 나서, page 구조체 자체를 해제해주면 됩니다.



```c
static void anon_destroy (struct page *page);
```

> 
> anon_destroy 함수는 익명 페이지를 지우는 함수입니다. 이 함수는 페이지 구조체의 vm field에 들어있는 정보를 이용해서 익명 페이지를 찾아내고, 그 페이지의 정보를 이용해서 익명 페이지에 대한 자원을 해제합니다. 이 함수는 익명 페이지를 이용한 메모리 매핑이 해제될 때 호출됩니다.
>
> 구체적으로는, 익명 페이지를 이용한 메모리 매핑을 해제할 때는 그 페이지가 이전에 할당된 프레임을 반환하고, 해당 프레임이 가리키는 물리 페이지도 해제해야 합니다. 이를 위해서는 먼저 프레임 번호를 얻어내고, 이 번호를 이용해서 프레임을 반환하고, 해당 프레임이 가리키는 물리 페이지를 해제합니다. 그리고 나서, 페이지 테이블에서 해당 페이지를 지우고, 페이지 테이블 자체의 크기도 축소합니다.

```c
void
anon_destroy(struct page *page)
{
    struct frame *frame;

    frame = page->frame;
    if (frame != NULL) {
        pframe_free(frame);
    }
    ptable_clear_page(page->thread->ptable, page->va);
    ptable_dec_size(page->thread->ptable);
}
```

여기서는 먼저 페이지의 frame 필드를 검사해서 해당 페이지에 연결된 프레임이 있는지 확인합니다. 프레임이 있다면, pframe_free 함수를 이용해서 해당 프레임을 반환합니다. 그리고 나서 페이지 테이블에서 해당 페이지를 지우고, 페이지 테이블의 크기를 축소합니다.

syscall process.c load lock acquir loack relase 

앞에있는 인자가 child, parent



위의 코드에서 fork-read는 실패하는 이유는 다음과 같습니다.

1. `supplemental_page_table_copy()` 함수는 `src`와 `dst`의 두 개의 `supplemental_page_table` 구조체를 복사합니다.
2. `src`와 `dst`는 모두 `hash_table`을 사용하여 페이지를 저장합니다.
3. `supplemental_page_table_copy()` 함수는 `src`의 `hash_table`을 순회하면서 각 페이지를 `dst`의 `hash_table`에 복사합니다.
4. `supplemental_page_table_copy()` 함수는 `src`와 `dst`의 `hash_table`을 모두 암호화합니다.
5. `fork()` 함수는 부모 프로세스의 복사본을 생성합니다.
6. 자식 프로세스는 부모 프로세스의 `hash_table`을 복사합니다.
7. 자식 프로세스는 부모 프로세스의 `hash_table`을 해독합니다.
8. 자식 프로세스는 부모 프로세스의 `hash_table`에서 페이지를 읽으려고 시도합니다.
9. 자식 프로세스는 부모 프로세스의 `hash_table`에서 페이지를 찾을 수 없습니다.
10. 자식 프로세스는 `EIO` 오류를 발생시킵니다.

이 문제를 해결하려면 `supplemental_page_table_copy()` 함수에서 `src`와 `dst`의 `hash_table`을 복사하기 전에 `src`의 `hash_table`을 해독해야 합니다.