from recommend import *

sample_text = "좋아하는 일로 행복하게 일하는 상위 1% 밀레니얼 프리워커 드로우앤드류입니다."
cleaned_text = preprocess.text_cleaning(sample_text)
noun_extract_text = preprocess.noun_extractor(cleaned_text)
keyword_noun_text = preprocess.keyword_extractor(noun_extract_text)
preprocess.word_2_vec(keyword_noun_text)
