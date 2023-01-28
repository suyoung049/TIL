from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb://test:test@13.209.50.82',27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def read_articles():
    result = list(db.memos.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'memos': result})

@app.route('/memo', methods=['POST'])
def post_memos():
    title_receive = request.form['title_give']
    text_receive = request.form['text_give']

    memo = {'title':title_receive, 'text':text_receive, 'id':''}
    db.memos.insert_one(memo)

    # 수정과 삭제를 위해 데이터 id를 string으로 변환하는 과정
    change_id = db.memos.find_one({'title':title_receive})
    myObjectId = change_id['_id']
    id_string = str(myObjectId)
    db.memos.update_one({"title":title_receive}, {"$set": {"id":id_string}})

    return jsonify({'result':'success'})

@app.route("/memo/delete", methods=["POST"])
def delete_memo():
    id_receive = request.form["id_give"]
    db.memos.delete_one({"id":id_receive})

    return jsonify({"result": "success"})

@app.route("/memo/change", methods=["POST"])
def chagne_memo():
    title_receive = request.form["title_give"]
    text_receive = request.form['text_give']
    id_receive = request.form['id_give']

    db.memos.update_one({"id": id_receive}, {"$set":{"title":title_receive}})
    db.memos.update_one({"id": id_receive}, {"$set":{"text":text_receive} })

    return jsonify({"result": "success"})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)