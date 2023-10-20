import re
from collections.abc import Mapping
import gensim
import pandas as pd
import numpy as np
from keybert import KeyBERT
from kiwipiepy import Kiwi

kiwi = Kiwi()
keyword_model = KeyBERT()

## remove special characters
def text_cleaning(text):
    text = re.sub(r"[^^a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣 ]", "", text)
    return text

## extract nouns
def noun_extractor(text):
    results = []
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
            results.append(token)
    return results

## extract keywords top 5
def keyword_extractor(noun_list):
    noun_text = ' '.join(noun_list)
    keyword_model.extract_keywords(noun_text, keyphrase_ngram_range=(1,1), top_n=5)
    return noun_text


## convert word to vector
def word_2_vec(word):
    vec = 0
    return vec




sample_text = "좋아하는 일로 행복하게 일하는 상위 1% 밀레니얼 프리워커 드로우앤드류입니다."
cleaned_text = text_cleaning(sample_text)
noun_extract_text = noun_extractor(cleaned_text)
keyword_noun_text = keyword_extractor(noun_extract_text)

w2v_model = gensim.models.Word2Vec.load('./recommend/model/ko.bin')
a = w2v_model.wv.most_similar("강아지")

w2v_model.wv["강아지"].shape
