from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('localhost',username='hakuna-gateway',password='hakuna-gateway',authSource='admin')
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
def getStarFromTile(title):
    star = db.movies.find_one({'title': title})['star']
    return star

def getTitlesFromTitle(title):
    star = getStarFromTile(title)
    movies = list(db.movies.find({'star': star}))
    titles = []
    for movie in movies:
        titles.append(movie['title'])
    return titles

for title in getTitlesFromTitle('주토피아'):
    print(title)
