from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost',username='test',password='test',authSource='admin')
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    articles = list(db.memos.find(projection={'_id': False}))
    print(articles)
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result':'success', 'articles': articles})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
	# 1. 클라이언트로부터 데이터를 받기
    url = request.form['url']
    comment = request.form['comment']
    print(url, comment)

	# 2. meta tag를 스크래핑하기
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url,headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    memo_dict = {
        'url': url,
        'comment': comment,
        'og_image': og_image['content'],
        'og_title': og_title['content'],
        'og_description': og_description['content'] 
    }

	# 3. mongoDB에 데이터 넣기
    db.memos.insert_one(memo_dict)

    return jsonify({'result': 'success', 'msg':'포스팅 되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)