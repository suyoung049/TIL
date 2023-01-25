from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle 

all_movies = list(db.movies.find({}))

# Q1. 영화제목 '매트릭스'의 평점을 가져오기

movie = db.movies.find_one({'title':'매트릭스'})
score = movie['star']

# Q2. '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기

same = list(db.movies.find({'star': score},{'_id':False}))

for i in same:
    print(i['title'])

# Q3. 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})
movie = db.movies.find_one({'title':'매트릭스'})
score = movie['star']
print(score)
