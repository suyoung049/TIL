## 02/08 mysql

# 다양한 데이터베이스의 특징

1. 데이터베이스의 원칙

   1. data integrity(무결성)
      1. 데이터가 전송, 저장, 처리되는 과정에서 변경되거나 손상되지 않는 것
      2. 완전성, 정확성, 일관성을 유지함
   2. data reliability (안전성)
      - 데이터를 보호할 수 있는 방법
      - 인증/인가되지 않은 사용자로부터 데이터를 보호함
      - 고장이 안나야됨
   3. scalability (확장성)
      - 데이터 양이나 사용자가 늘어날 때 대처 가능

2. 데이터베이스 종류

   1. relational
      1. 데이터를 row와 column으로 이루어진 table의 형태로 저장함
      2. SQL(Structured Query Language)를 사용해서 데이터를 읽어오거나 조작함
      3. MySQL, Oracle, Postgre 등이 해당
   2. key-value
      1. key-value pair로 데이터를 저장
      2. key는 unique identifier로도 사용됨
      3. redis등이 해당
         - cache
         - message broker → pub/sub
         - not that scalable → limitation on the size of RAM
         - Dynamo DB
           - partiton key - primary.
           - sort key - secondary, optional
           - advantage
             - scalable →AWS offers, HA, serverless
   3. graph
      1. 데이터를 graph의 형태로 저장
      2. 각 항목이 node로 이루어져있고, node간의 관계는 edge를 사용해서 나타냄\d
         1. 알고리즘 보면 뭐와 뭐간의 거리 이런것
      3. SNS등 서로 관계가 복잡한 상황에서 자주 사용됨
      4. Neo4j, OrientDB등이 해당
      5. 링크드인 - 1촌, 2촌,
   4. document
      1. document database라고도 함
         1. 구조가 완전 자유로움
      2. row, column과 같은 구조는 없고 자유로운 형태로 데이터를 저장함
         - 일반적으로 JSON 또는 XML 형태
      3. 데이터베이스별로 데이터를 조작할 수 있는 언어가 따로 있음
      4. MongoDB, CassandraDB, Couchbase 등이 해당
      5. 형식이 자유로워야 할 때??
         - 블로그 포스트. 사진이 언제 몇개가 들어갈 지 모르는??
   5. row-oriented vs column-oriented
      1. row - mysql, postgre, hbase
      2. column - cassandra, hbase, BigQuery
      3. example - Netflix - 2.3억명2

3. 서비스에 적합한 데이터베이스 선택법

   1. CAP Theorem

      ![캡테마](0208 mysql.assets/캡테마.png)

      - consistency(일관성)
        - 데이터베이스 안의 모든 node들이 같은 값을 가지고 있음
        - request를 보내면 해당 request가 delay 될 수 있음
        - 금융 쪽에서 중요하게 생각함
        - 송금 데이터가 데이터베이스 노드당 align되지 않으면? 송금 안된줄 알고 또보내고 또보내고….
      - availability(가용성)
        - 데이터베이스에 request를 보내면 항상 response를 받음
          - consistencty는 response바로 안옴
        - 하지만 해당 response가 가장 최근 데이터라는 것을 보장받을 수 없음
        - 접근하는 node에 따라 값이 다르다
      - partition-tolerance(분산처리)
        - node간 소통이 불가능 하더라도 정상적으로 작동함
      - C - P // A - P // C - A

   2. 3가지를 다 가질 수는 없음. 왜냐면…

   ![데이터클라우드](0208 mysql.assets/데이터클라우드.png)

   예시

   - RDBMS - Netflix
     - 영상에 대한 정보를 저장하는 방식
     - 평점 데이터를 가져와서 인공지능과 연결 아마도??  → 사용자가 좋아할 것 같은 영상을 추천한다
   - NoSQL - 인스타그램
     - [Cassandra DB 블로그](https://jasonkang14.github.io/database/cassandra-db)↗️
     - 종종 데이터 날아가는데 몇시간 뒤에 복구함 어떻게 이게 가능한지?
     - 데이터를 저장하는 방식 덕분에/때문에 가능하다

4.관계형 데이터베이스(RDBMS) vs 비관계형 데이터베이스(NoSQL)

a. scale up vs scale out

![표정리](0208 mysql.assets/표정리.png)

![스케일인아웃](0208 mysql.assets/스케일인아웃.png)
