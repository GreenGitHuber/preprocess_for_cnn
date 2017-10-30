# -*- coding:utf-8 -*-
#!/usr/bin/python
import pandas as pd 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

model = Word2Vec.load('../model/wiki.zh.text.model')
#print (model.wv['◆'].shape)
print (type(model.wv['我']))
