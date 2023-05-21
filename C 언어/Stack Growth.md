## Stack Growth

프로젝트 2에서 stack 은 USER_STACK을 기준으로 한 페이지로 구성, 프로그램 실행은 이 크기로 제한 되었다. 그러나 이제 stack이 크기를 초과하면 필요에 따라 추가 페이지를 할당

만약 스택 접근 처럼 보인다면 추가페이지를 할당, 스택 접근과 다른 접근을 구분하려는 휴리스틱을 개발하십시오.

유저 프로그램은 스택 포인터 아래에 쓰기를 하면 버그가 발생할 수 있습니다. 왜냐하면 일반적인 실제 운영체제는 "신호(signal)"를 전달하기 위해 언제든지 프로세스를 중단할 수 있기 때문에 스택의 데이터가 수정되기 때문입니다. 그러나 x86-64 PUSH 명령은 스택 포인터를 조정하기 전에 접근 권한을 학인하기 때문에 스택 포인터에서 8바이트 아래에서 페이지 폴트(page-fault)를 발생시킬 수 있습니다.

유저 프로그램의 스택 포인터의 현재 값을 얻을 수 있어야 합니다. 시스템 호출 내에서 또는 유저 프로그램이 생성한 페이지 폴트에서는 각각 syscall_handler() 또는 page_fault()에 전달된 struct intr_frame의 rsp 멤버에서 해당 값을 검색할 수 있습니다. 유효하지 않은 메모리 접근을 감지하기 위해 페이지 폴트에 의존하는 경우, 커널에서 페이지 폴트가 발생하는 경우를 처리해야 합니다. 프로세서는 예외가 사용자 모드에서 커널 모드로 전환될 때만 스택 포인터를 저장하므로, page_fault()에 전달된  struct intr_frame 에서 rsp를 읽으면 정의되지 않은 값이 반환되며 유저 스택 포인터가 아닙니다. 따라서 최초의 사용자 모드에서 커널 모드에서 커널 모드로의 전환 시점에 rsp를 struct thread에 저장하는 다른 방법을 마런해야 한다.

스택 확장 기능을 구현하세요. 이를 위해 먼저 vm/vm.c의 vm_try_handle_fault를 수정하여 스택확장을 식별합니다. 스택 확장을 식별한 후, vm/vm.c의 vm_stack_growth를 호출하여 스택을 확장해야 합니다. vm_stack_growth를 구현하세요.



```c
bool vm_try_handle_fault (struct intr_frame *f, void *addr,
    bool user, bool write, bool not_present);
```

> 이 함수는 userprog/exception.c의 page_fault에서 페이지 폴트 예외 처리 중에 호출됩니다. 이 함수에서는 페이지 폴트가 스택 확장의 유효한 경우인지 확인해야 합니다. 폴트를 스택 확장으로 처리할 수 있다고 확인한 경우, vm_stack_growth를 호출하여 폴트가 발생한 주소와 함께 호출해야 합니다.

1. f : 시스템 콜 또는 페이지 폴트가 발생했을 때,그 순간의 레지스터 값들을 담고 있는 구조체.
2. addr : 페이지 폴트를 일으킨 가상 주소
3. user : 해당 값이 true일 경우 현재 쓰레드가 유저 모드에서 돌아가다가 페이지 폴트를 일으켰음을 나타낸다.즉,현재 쓰레드의 rsp값이 VM의 유저 영역을 나타내는지 커널 영역을 나타내는지를 알려준다.
4. write : true일 경우,해당 페이지 폴트가 쓰기 요청이고 그렇지 않을 경우 읽기 요청을 나타냄
5. not-present : 해당 인자가 false인 경우는 read-only 페이지에 write를 하려는 상황을 나타냄.주어진 테스트 케이스에서는 `mmap-ro` 케이스가 해당 인자를 체크함



```c
void vm_stack_growth (void *addr);
```

> 주어진 주소(addr)를 페이지 크기(PGSIZE)로 내림하여 할당된 익명 페이지를 사용하여 스택 크기를 증가시킵니다.



대부분의 운영 체제는 스택 크기에 절대적인 제한을 둡니다. 일부 운영 체제는 사용자가 조정할 수 있는 제한을 가지며, 예를 들어 많은 유닉스 시스템에서는 ulimit 명령으로 조정할 수 있습니다. 많은 GNU/Linux 시스템에서는 기본 제한이 8MB입니다. 이 프로젝트에서는 스택 크기를 최대 1MB로 제한해야 합니다. 



curr->rsp  : 커널 영역

intr_frame = 유저 영역



```c
#define pg_round_down(va) (void *) ((uint64_t) (va) & ~PGMASK) 

/*pg_round_down() 함수는 주어진 주소를 가장 가까운 페이지 경계로 내림합니다. 예를 들어, pg_round_down(0x100010)은 0x100000을 반환합니다.

이 함수는 PGMASK 상수로 정의된 페이지 마스크를 사용하여 주소를 내림합니다. 페이지 마스크는 페이지 경계의 비트가 0이고 나머지 비트가 1인 64비트 정수입니다. 예를 들어, PGMASK는 0xFFFFFFFFFFFFF000입니다.

함수는 (uint64_t) (va) & ~PGMASK 연산을 사용하여 주소를 내림합니다. 이 연산은 주소의 하위 12비트를 0으로 설정합니다. 예를 들어, (uint64_t) (0x100010) & ~PGMASK은 0x100000을 반환합니다.*/


```



```c
if (rsp_stack-8 <= addr  && USER_STACK - 0x100000 <= addr && addr <= USER_STACK){
				vm_stack_growth(pg_round_down(addr));
		} 
/*
```

lenth = load readbyetes file syze

​							

