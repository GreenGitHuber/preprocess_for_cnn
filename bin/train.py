# -*- coding :utf-8 -*-

import pandas as pd 
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

model = Word2Vec.load('wiki.zh.txt.model')
print model.wv['我']