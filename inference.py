from gensim import models

ko_model = models.fasttext.load_facebook_model('model/cc.ko.300.bin/cc.ko.300.bin')

for w, sim in ko_model.wv.most_similar('파이썬'):
    print(f'{w}: {sim}')

print(ko_model.wv.similarity("코딩", '파이썬'))
print(ko_model.wv.similarity("파이썬", '자바'))
print(ko_model.wv.similarity("파이썬", '딥러닝'))
print(ko_model.wv.similarity("자바스크립트", '자바'))
print(ko_model.wv.similarity("아이스크림", '컴퓨터'))

for w, sim in ko_model.wv.most_similar('UX'):
    print(f'{w}: {sim}')

print(ko_model.wv.similarity("UX", 'UI'))

