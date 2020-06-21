import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
# 용어별 링크에 접근하기 위한 Seq.번호를 가져오기 
def get_word_seq():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.post('https://terms.tta.or.kr/dictionary/dictionaryNewWordList.do', headers=headers, data={'listPage':1})
    soup = BeautifulSoup(data.text, 'html.parser')
    each_page = soup.select('#m_content > ul > li > dl')
    word_seqs =[]
    for one in each_page:
        word_seq = one.select('dl > dt > a')[0]['href']
        word_seq = word_seq[-10:-2]
        word_seqs.append(word_seq)
    #print(word_seqs)
    return word_seqs
# word_seqs = get_word_seq()
# Seq.번호별로 용어 설명 페이지에서 용어/설명/이미지를 가져 옵니다. 
def get_term():
    termlists= ['171384-2'] #get_word_seq()
    print(termlists)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    for termlist in termlists:
        print(termlist)
        data = requests.post('https://terms.tta.or.kr/dictionary/dictionaryView.do', headers=headers, data={'word_seq':termlist})
        soup = BeautifulSoup(data.text, 'html.parser')
        #each_term = soup.select('#cont > dl')[0].text.strip()  # #cont > dl
        each_term = soup.select_one('#cont > dl > dt').text.strip() 
        each_desc = soup.select_one('#cont > dl > dd > div').text.strip() 
        each_img = soup.select_one('#cont > dl > dd > div').find('img')['src']
        print(each_term)
        print(each_desc)
        print(each_img)
get_term()