#  원격저장소에 로컬저장소의 커밋 push하기

1. GitHub에서 원격 저장소 만들기

2. 로컬 저장소에 원격저장소 경로 추가

   ``` bash
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/0706 (master)
   $ git remote add origin https://github.com/suyoung049/test.git
   ```

   

3.  원격 저장소의 정보 확인

   ```bash
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/0706 (master)
   $ git remote -v
   origin  https://github.com/suyoung049/test.git (fetch)
   origin  https://github.com/suyoung049/test.git (push) 
   ```

   

4.  원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림

   ```bash
   holho@DESKTOP-7SL46VG MINGW64 ~/OneDrive/바탕 화면/0706 (master)
   $ git push origin master
   Enumerating objects: 3, done.
   Counting objects: 100% (3/3), done.
   Delta compression using up to 6 threads
   Compressing objects: 100% (2/2), done.
   Writing objects: 100% (2/2), 220 bytes | 220.00 KiB/s, done.
   Total 2 (delta 1), reused 0 (delta 0), pack-reused 0        
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/suyoung049/test.git
      cdc1cf7..3905392  master -> master
   ```

   