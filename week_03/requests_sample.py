import requests

# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
# print(rjson['RealtimeCityAir']['row'][0]['NO2'])


r = requests.post(url="https://terms.tta.or.kr/mobile/dictionaryNewWordList.do", data={"listPage": 1})
print(r.content.decode('utf-8'))
