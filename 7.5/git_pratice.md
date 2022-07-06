# 저장소 만들기

1. 바탕화면에 특정 폴더 생성

2. 문서 생성

   ```bash
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/Test
   $ touch 1.txt
   
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/Test
   $ touch 2.txt
   ```

3. 특정 폴더를 git 저장소(repositoty)로 만들어 git으로 관리(master 생성 확인)

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/holho/OneDrive/바탕 화면/Test/.git/
   
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/Test (master)
   ```

   

4.  working directory상의 변경내용을 staging area에 추가

   ```bash
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/Test (master)
   $ git add 1.txt
   
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/Test (master)
   $ git add 2.txt
   ```

   

5. 추가 되었는지 상태 확인

   ```bash
   $ git status
   On branch master
   
   No commits yet
   
   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
           new file:   1.txt
           new file:   2.txt
   ```

   

6. staged 상태의 파일들을 커밋을 통해 버전으로 기록

   ```bash
   $ git commit -m TEST
   [master (root-commit) 34fd8d8] TEST
    2 files changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 1.txt
    create mode 100644 2.txt
   ```

   

7. 저장소에 기록된 커밋을 조회

   ```bash
   $ git log
   commit 34fd8d889a1e0b7f6d312b2ed17e193c879afb74 (HEAD -> master)
   Author: suyoung049 <suyoung049@gmail.com>
   Date:   Wed Jul 6 17:22:44 2022 +0900
   
       TEST
   ```

   
