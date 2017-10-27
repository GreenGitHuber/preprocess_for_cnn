#-*- coding=utf8 -*-
import jieba
import nltk
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#上面两句在python3已经取消了
#import importlib
#importlib.reload(sys)
import jieba.analyse
#创建停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r').readlines()]
    return stopwords

#增加了自定义词典的分词系统
def main():
    USAGE = "usage:    python preprocess.py [file name] -k [top k]"
    raw = open(r"zhaospam.txt")
    #载入外部字典
    line = raw.readline()
    str = ''
    while line:
        string = re.sub("[\！\？\*\~\)\/\(\-\;\:P\“\”\[\]\%]".decode("utf8"), "".decode("utf8"), line)
        string = re.sub("[\=\=\、\：\:\！\？\【 \】 \% \。\，\“\” \～ … \# \?\!\.\,\:\《\》]".decode("utf8"), "".decode("utf8"), string)
        string = re.sub('[\w+\d]', "".decode("utf8"), string)
        str += string
        line = raw.readline()
    raw.close()
    seg_list=jieba.cut(str,cut_all=False)
    #stopwords = stopwordslist("extra_dict/stop_words.txt")
    #for word in seg_list:
     #   if word not in stopwords:
    str=" ".join(seg_list)
    f=open("zhaospam_af_jieba.txt",'wb')
    f.write(str)
    f.close()

if __name__ == "__main__":
    main()
