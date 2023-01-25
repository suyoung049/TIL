from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/memo', methods=['GET'])
# def listing():
#     return jsonify({'result':'success', 'msg':'GET 연결되었습니다.'})

# @app.route('/memo', method=['POST'])
# def saving():
#     return jsonify({'result':'success', 'msg':'POST 연결되었습니다.'})

    
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)