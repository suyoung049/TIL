



## Page Structure and Operations

### 과제개요



-  Supplemental page table 구현하기

  - 기존 pintos 에서는 pml4 페이지 테이블 제공
  - 가상메모리를 구현하기에는 부족
  - 주어진 va 에 대한 kva로의 단순 변환만 해주고있음
  -  이는 사용할 struct page에 대한 정보가 없는 것
  - SPT는 각 page에 대한 정보를 추가해 보중하는 역활

- SPT 목적 1번

  - page fault 발생 시, 해당 page fault 가 발생한 page 찾기
  - 찾은 page가 갖고 있는 여러 데이터들에 접근하기 위해

- SPT 목적 2번

  - 커널이 process(or thread)를 종료시킬 때, 해당 SPT 를 참고해 어떤 데이터를 할당 해제 할지 결정
  - page fault가 일어난 va 를 포함하는 struct page에 접근해 다양한 데이터 사용 가능

  

### struct page

include/vm/vm.h에 정의된 페이지는 가상 메모리의 페이지를 나타내는 구조체입니다. 페이지에 대해 알아야하는 모든 필요한 데이터를 저장합니다. 현재, 템플릿에서 다음과 같이 구조체가 정의되어 있습니다:



```c
struct page {
  const struct page_operations *operations;
  void *va;              /* Address in terms of user space */
  struct frame *frame;   /* Back reference for frame */

  union {
    struct uninit_page uninit;
    struct anon_page anon;
    struct file_page file;
#ifdef EFILESYS
    struct page_cache page_cache;
#endif
  };
};
```



include/vm/vm.h에 정의된 페이지는 가상 메모리의 페이지를 나타내는 구조체입니다. 페이지에 대해 필요한 모든 정보를 저장합니다. 현재 템플릿에서는 다음과 같은 구조체로 나타납니다:

구조체에는 페이지 연산(read below), 가상 주소, 물리 프레임이 있습니다. 또한, union 필드가 있습니다. union은 다른 유형의 데이터를 메모리 영역에 저장할 수 있는 특수한 데이터 유형입니다. 여러 멤버가 있지만 한 번에 하나의 멤버만 값을 포함할 수 있습니다. 이는 시스템의 페이지가 uninit_page, anon_page, file_page 또는 page_cache일 수 있다는 것을 의미합니다. 예를 들어, 페이지가 익명 페이지인 경우(익명 페이지 참조), 페이지 구조체에는 struct anon_page anon 필드가 하나의 멤버로 포함됩니다. anon_page는 익명 페이지에 대해 유지해야 하는 모든 필요한 정보를 포함합니다.



### Page Operations

위에서 설명한 대로, vm.h 파일에 정의된 대로, 페이지는 VM_UNINIT, VM_ANON 또는 VM_FILE 일 수 있습니다. 페이지마다 스왑 인, 스왑 아웃 및 페이지 파괴와 같은 여러 작업이 필요합니다. 각 유형의 페이지에 대해 필요한 단계와 작업이 다르기 때문에 VM_ANON 페이지와 VM_FILE 페이지에 대해 각각 다른 destroy 함수를 호출해야합니다. 이를 처리하기 위해 switch-case 구문을 각 함수에서 사용하는 방법이 있습니다. 우리는 "객체 지향 프로그래밍"의 "클래스 상속" 개념을 도입합니다. 실제로 C 프로그래밍 언어에는 "클래스"나 "상속"이 없으며, 우리는 함수 포인터를 사용하여 개념을 구현합니다. 이는 리눅스와 같은 실제 운영 체제 코드에서도 비슷하게 사용됩니다.

함수 포인터는 메모리 내부에 있는 함수 또는 실행 가능한 코드를 가리키는 다른 포인터들과 마찬가지로 포인터입니다. 함수 포인터는 실행 시간 값에 따라 특정 함수를 호출하여 실행하는 간단한 방법을 제공하기 때문에 유용합니다. 우리 경우에는, 단순히 `destroy(page)`를 호출하면 코드 수준에서 충분하며, 컴파일러는 함수 포인터를 통해 페이지 유형에 따라 적절한 destroy 루틴을 선택하여 호출합니다.

include/vm/vm.h에 정의된 page_operations 구조체는 함수들의 테이블로 생각할 수 있습니다. 이 구조체는 세 개의 함수 포인터를 포함하고 있습니다

```c
struct page_operations {
  bool (*swap_in) (struct page *, void *);
  bool (*swap_out) (struct page *);
  void (*destroy) (struct page *);
  enum vm_type type;
};
```

이제, page_operations 구조체가 어디에서 찾을 수 있는지 알아봅시다. include/vm/vm.h의 page 구조체를 살펴보면, operations이라는 필드가 있음을 알 수 있습니다. 이제 vm/file.c로 가보면, 함수 원형 전에 선언된 page_operations 구조체 file_ops를 볼 수 있습니다. 이것은 파일 지원 페이지에 대한 함수 포인터 테이블입니다. .destroy 필드는 file_backed_destroy라는 페이지를 파괴하는 함수를 가리키며, 같은 파일에서 정의됩니다.

file.c 파일에 선언된 file_ops 구조체를 보면, destroy 필드가 file_backed_destroy 함수를 가리키고 있음을 알 수 있습니다. 그렇다면, file_backed_destroy 함수가 어떻게 함수 포인터 인터페이스를 이용해서 호출되는지 알아보겠습니다. 만약 vm_dealloc_page(page) 함수가 호출되고, 이 page가 파일 백드 페이지 (VM_FILE)인 경우를 가정해봅시다. 함수 내에서 destroy(page)를 호출합니다. destroy(page)는 다음과 같이 include/vm/vm.h 파일에 매크로로 정의되어 있습니다:

```c
#define destroy(page) if ((page)->operations->destroy) (page)->operations->destroy (page)
```

이는 destroy 함수를 호출하면 실제로 (page)->operations->destroy (page)가 호출되며, 이는 페이지 구조체에서 검색된 destroy 함수를 호출합니다. 페이지가 VM_FILE 페이지인 경우, 해당 페이지의 .destroy 필드는 file_backed_destroy를 가리킵니다. 따라서 파일을 기반으로 한 페이지의 destroy 루틴이 수행됩니다.



### Implement Supplemental Page Table

#### 과제 개요

- Frame 구조체의 kva는 물리메모리와 1대1로 매핑된다.
  - 따라서 무릴 메모리의  kernel에 kva로 바로 접근 가능
- 가상 메모리는 크게 유저 영역과 커널 영역으로 나뉘고, 커널 영역은 User pool과 Kernel pool로 나뉜다. 또 커널영역은 물리메모리와 1대1로 매핑된다.
  - virtual memory = user area + kernel area
  - kernel area = user pool + kernel pool
- `palloc_get_page(PAL_USER)` 는 커널역역의 User_Pool 영역에서 물리 메모리를 할당 하여 kva값을 반환
- page 구조체의 va + KERNBASE = kva라는 공식이 성립 된다.
- 

이 시점에서, Pintos는 가상 및 물리 메모리 매핑을 관리하기 위한 페이지 테이블(pml4)을 가지고 있습니다. 하지만 이것만으로는 충분하지 않습니다. 이전 섹션에서 논의한 대로, 페이지 폴트와 리소스 관리를 처리하기 위해 각 페이지에 대한 추가 정보를 보유하는 보조 페이지 테이블도 필요합니다. 따라서 프로젝트 3의 첫 번째 작업으로 보조 페이지 테이블의 일부 기본 기능을 구현하는 것이 좋습니다.

**vm/vm.c에 보조 페이지 테이블 관리 함수를 구현하세요.**

먼저 Pintos에서 보조 페이지 테이블을 어떻게 설계할지 결정해야 합니다. 자신만의 보조 페이지 테이블을 디자인한 후, 다음 세 가지 함수를 구현하세요.

```c
void supplemental_page_table_init (struct supplemental_page_table *spt);
```

> Supplemental page table을 초기화하는 함수입니다. 어떤 데이터 구조를 사용할지는 여러분이 결정할 수 있습니다. 이 함수는 새로운 프로세스가 시작될 때(initd in userprog/process.c)와 프로세스가 복제될 때(__do_fork in userprog/process.c) 호출됩니다.

```c
struct page *spt_find_page (struct supplemental_page_table *spt, void *va);
```

> 주어진 보조 페이지 테이블에서 va에 해당하는 struct page를 찾습니다. 찾지 못하면 NULL을 반환합니다.

```c
bool spt_insert_page (struct supplemental_page_table *spt, struct page *page);
```

> 주어진 보조 페이지 테이블에 구조체 페이지를 삽입합니다. 이 함수는 가상 주소가 주어진 보조 페이지 테이블에 존재하지 않는지 확인해야 합니다.



### Frame Management

이제부터 모든 페이지는 구성 시기의 메모리의 메타데이터만을 보유하는 것이 아닙니다. 그러므로 물리 메모리를 관리하기 위한 다른 방식이 필요합니다. include/vm/vm.h에는 물리 메모리를 나타내는 struct frame이 존재합니다. 현재, 이 구조체는 다음과 같이 보입니다:

``` c
/* The representation of "frame" */
struct frame {
  void *kva;
  struct page *page;
};
```

이 구조체는 오직 두 개의 필드만 가지고 있습니다. 하나는 커널 가상 주소인 kva이고, 다른 하나는 페이지 구조체인 page입니다. 더 많은 멤버를 추가하여 프레임 관리 인터페이스를 구현할 수 있습니다.

**vm/vm.c에서 vm_get_frame, vm_claim_page 및 vm_do_claim_page를 구현하세요.**

```c
static struct frame *vm_get_frame (void);
```

> palloc_get_page를 호출하여 사용자 풀에서 새 물리 페이지를 가져옵니다. 사용자 풀에서 페이지를 성공적으로 가져오면 프레임을 할당하고 멤버를 초기화한 다음 반환합니다. vm_get_frame을 구현한 후에는 모든 사용자 공간 페이지(PALLOC_USER)를 이 함수를 통해 할당해야 합니다. 페이지 할당 실패 시 스왑 아웃 처리를 현재는 다룰 필요가 없습니다. 그저 PANIC("todo")로 표시하면 됩니다.

``` c
bool vm_do_claim_page (struct page *page);
```

> 주장(claim)은 물리적인 프레임, 페이지를 할당하는 것을 의미합니다. 먼저 vm_get_frame 함수를 호출하여 프레임을 얻어야 합니다. 그런 다음 MMU를 설정해야 합니다. 즉, 가상 주소에서 물리적 주소로의 매핑을 페이지 테이블에 추가해야 합니다. 반환 값은 작업이 성공했는지 여부를 나타내야 합니다. 이 작업은 이미 템플릿에서 완료되었습니다.

```c

static struct frame *vm_get_frame (void) {
    void *kpage = palloc_get_page(PAL_USER);
    if (kpage == NULL) {
        PANIC("todo");
    }

    struct frame *frame = malloc(sizeof(struct frame));
    if (frame == NULL) {
        palloc_free_page(kpage);
        PANIC("todo");
    }

    frame->kpage = kpage;
    frame->thread = thread_current();
    frame->upage = NULL;

    list_push_back(&frame_table, &frame->elem);

    return frame;
}
```

```c
bool vm_claim_page (void *va);
```

> 할당할 페이지를 요청합니다 `va`. 먼저 페이지를 가져온 다음 페이지와 함께 vm_do_claim_page를 호출해야 합니다.

