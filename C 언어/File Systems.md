## File Systems



### Indexed and Extensible Files

기본 파일 시스템은 파일을 단일 익스텐트로 할당하기 때문에 외부 조각화에 취약하다. on-disk inode 구조를 수정하여 이문제를 제거해야 합니다

** 참고 **

파일 시스템 파티션이 8MB보다 크지 않을 것이라고 가정할 수 있습니다. 파티션 만큼 큰 파일을 지원해야 합니다. 각 inode는 하나의 디스크 섹터에 저장되어 포함 될 수 잇는 블록 포인터의 수를 제한합니다.



##### Indexing large files with FAT (File Allocation Table)

 이전 프로젝트에서 사용했던 기본 파일 시스템에서 파일은 여러 디스크 섹터에 연속적인 단일 청그로 저장되었습니다. 클러스터(청크)는 하나 이상의 연속 디스크 섹터를 포함할 수 있으므로 연속 청크를 클러스터라고 부르겠습니다. 이러한 관점에서 파일 시스템의 클러스터 크기는 클러스터에 저장된 파일의 크기와 동일했습니다. 

외부 조각화를 완화 하기 위해 클러스터 크기를 줄일 수 있습니다.(가상메모리의 페이지 크기를 기억하십시오.) 단순화를 위해 스켈레톤 코드에서 클러스터의 섹터수를 "i" 이와 같이 더 작은 클러스터를 사용하면 클러스터가 전체 파일을 저장하기에 충분하지 않을 수 있습니다. 이 경우 파일에 대해 여러 클러스터가 필요하므로 inode의 파일에 대한 클러스터를 인덱싱할 데이터 구조가 필요합니다. 가장 쉬운 방법중 하나는 변경된 목록(일명 체인)을 사용하는 것입니다. inode는 파일의 첫 번째 블록의 섹터 번호를 포함 할 수 있으며, 첫 번째 블록은 두 번째 블록의 섹터 번호를 포함 할 수 있습니다. 그러나 이 순진한 접근 방식은 파일의 모든 블록을 읽어야 하기 때문에 너무 느립니다. 이를 극복하기 위해 FAT(파일 할당 테이블)는 블록 자체가 아닌 고정된 크기의 파일 할당 테이블에 블록의 연결성을 부여합니다. FAT는 실제 데이터가 아닌 연결 값만 담고 있기 때문에 DRAM에 캐싱할 수 있을 정도로 크기가 작습니다. 결과적으로 테이블에서 해당 항목을 읽을 수 있습니다.

제공된 스켈레톤 코드를 사용하여 inode 인덱싱을 구현합니다. `filesys/fat.c` 이 섹션에서는 do에 이미 구현된 기능 fat.c 에 구현해야 하는 기능데 대해 간략하게 설명합니다.

  6가지 기능은 `fat.c`부팅 `fat_init()`시 `fat_open()`디스크 `fat_close()`를 초기화 및 포맷하므로 수정할 필요가 없습니다 `fat_create()`. `fat_boot_create()`그러나 작성해야 하며 `fat_fs_init()`그들이 하는 일을 간략하게 이해하면 도움이 될 수 있습니다.

```c
cluster_t fat_fs_init (void);
```

> FAT 파일 시스템을 초기화 합니다. `fat_fs` 의 `fat_length`  및 `data_start` 필드를 초기화해야 합니다. `fat_length` 는 파일 시스템 내의 클러스터 수를 저장하고, `data_start` 는 파일을 저장하기 시작할 수 있는 섹터를 저장합니다. `fat_fs->bs` 에 저장된 일부 값을 활용할 수 있습니다. 또한, 이 함수에서 다른 유용한 데이터를 초기화 할 수 있습니다.



 ```c
 cluster_t fat_create_chain (cluster_t clst);
 ```

> clst에서 지정된 클러스터 뒤에 클러스터를 추가하여 체인을 확장합니다. clst가 0과 같나면 새로운 체인을 생성합니다. 새로 할당된 클러스터의 클러스터 번호를 반환합니다.



```c
void fat_remove_chain (cluster_t clst, cluster_t pclst);
```

> clst에서 시작하여 체인에서 클러스터를 제거합니다. pclst는 체인에서 직전 클러스터여야 합니다. 즉, 이 함수의 실행 후에 pclst 는 업데이트 된 체인의 마지막 요소여야 합니다. clst가 체인의 첫번째 요소인 경우, pclst는 0이여야 합니다.



```c
void fat_put (cluster_t clst, cluster_t val);
```

> 클러스터 번호 clst가 가리키는 FAT 항목을 val로 업데이트 합니다. FAT의 각 항목은 체인에서 다음 클러스터를 가리킵니다.(있는 경우) 그렇지 않으면 EOChain을 가리킵니다. 이를 통해 연결성을 업데이트 하는 데 사용 할 수 있습니다.



```c
cluster_t fat_get (cluster_t clst);
```

> 주어진 클러스터 clst가 가리키는 클러스터 번호를 반환합니다.



```c
disk_sector_t cluster_to_sector (cluster_t clst);
```

> 클러스터 번호 clst를 해당하는 섹터 번호로 변환하고 섹터 번호를 반환합니다.



#### File Growth

**확장 가능한 파일을 구현합니다.** 기본 파일 시스템에서 파일 크기는 파일이 생성될 때 지정됩니다. 그러나 대부분의 최신 파일 시스템에서는 파일이 처음에 크기 0으로 생성된 다음 파일의 끝에서 쓰기가 이루어질 때마다 확장됩니다. 파일 시스템에서 이를 허용해야 합니다.

파일이 파일 시스템 크기(메타데이터 제외)를 초과할 수 없다는 점을 제외하고는 파일 크기에 미리 정해진 제한이 없어야 합니다. 이는 루트 디렉터리 파일에도 적용되며 이제 초기 제한인 16개 파일을 넘어 확장할 수 있습니다.

사용자 프로그램은 현재 EOF(파일 끝) 이상을 찾을 수 있습니다. 검색 자체는 파일을 확장하지 않습니다. EOF 이후의 위치에서 쓰기는 파일을 쓰고 있는 위치로 확장하며 이전 EOF와 쓰기 시작 사이의 간격은 0으로 채워야 합니다. EOF 이후의 위치에서 시작하는 읽기는 바이트를 반환하지 않습니다.

EOF 이상으로 작성하면 많은 블록이 완전히 0이 될 수 있습니다. 일부 파일 시스템은 암시적으로 0이 된 블록에 대해 실제 데이터 블록을 할당하고 씁니다. 다른 파일 시스템은 명시적으로 기록될 때까지 이러한 블록을 전혀 할당하지 않습니다. 후자의 파일 시스템은 "스파스 파일"을 지원한다고 합니다. 파일 시스템에서 할당 전략 중 하나를 채택할 수 있습니다.
