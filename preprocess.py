import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
from tqdm import tqdm

train_data = pd.read_table('data/ratings.txt')
train_data[:5] # 상위 5개 출력

train_data = train_data.dropna(how = 'any') # Null 값이 존재하는 행 제거

# 정규 표현식을 통한 한글 외 문자 제거
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True)


test_data = pd.read_csv('data/sample_description.csv', encoding="CP949")
test_data["message"] = test_data["message"].str.replace("[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣 ]","",regex=True)
test_data["description"] = test_data["description"].str.replace("[^0-9a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣 ]","",regex=True)

# 불용어 정의
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# 형태소 분석기 OKT를 사용한 토큰화 작업 (다소 시간 소요)
okt = Okt()
tokenized_data = []
for sentence in tqdm(train_data['document'][0:10]):
    tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
    stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    tokenized_data.append(stopwords_removed_sentence)

okt = Okt()
tokenized_data = []
for sentence in tqdm(test_data['description'][0:2]):
    print(sentence)
    tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
    stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    tokenized_data.append(stopwords_removed_sentence)

tokenized_data[5]