from pymongo import MongoClient

#client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('localhost',username='hakuna-gateway',password='hakuna-gateway',authSource='admin')
db = client.dbsparta # 'dbsparta'라는 이름의 db를 만듭니다.

all_users = list(db.users.find())
print(all_users)

condition_users = list(db.users.find({'age': 21}))
# print(condition_users)
# print(condition_users[0]['name'])

# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})