from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('localhost',username='hakuna-gateway',password='hakuna-gateway',authSource='admin')
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

'''
매트릭스의 평점과 같은 평점의 영화 제목들의 평점을 0으로 만들기
'''
def getStarFromTitle(title):
    star = db.movies.find_one({'title': title})['star']
    return star

def updateStarFromTitle(title):
    star = getStarFromTitle(title)
    db.movies.update_many({'star': star}, {'$set': {'star': 0}})

updateStarFromTitle('클래식')
