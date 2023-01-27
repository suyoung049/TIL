from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@13.209.50.82',27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})

@app.route('/memo', methods=['POST'])
def post_articles():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    
    data = requests.get(url_receive,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_image = og_image['content']
    url_title = og_title['content']
    url_description = og_description['content']

    article = {'url':url_receive, 'title':url_title, 'image':url_image, 'desc':url_description, 'comment':comment_receive}
    db.articles.insert_one(article)

    return jsonify({'result':'success'})

    
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)