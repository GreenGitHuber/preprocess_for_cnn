#-*- coding=utf8 -*-
import jieba
import nltk
import re
import jieba.analyse
#创建停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r').readlines()]
    return stopwords

#增加了自定义词典的分词系统
def main():
    USAGE = "usage:    python preprocess.py [file name] -k [top k]"
    raw = open(r"../corpus/zhaospam.txt")
    #载入外部字典
    line = raw.readline()
    str = ''
    while line:
        string = re.sub("[\！\？\*\~\)\/\(\-\;\:P\“\”\[\]\%]", "", line)
        string = re.sub("[\=\=\、\：\,\+\-\:\！\？\【\◆ \】 \% \。\，\“\” \～ … \# \?\!\.\,\:\《\》]", "", string)
        string = re.sub('[a-zA-Z\d]', "", string)
        str += string
        line = raw.readline()
    raw.close()
    seg_list=jieba.cut(str,cut_all=False)
    #stopwords = stopwordslist("extra_dict/stop_words.txt")
    #for word in seg_list:
     #   if word not in stopwords:
    str=" ".join(seg_list)
    f=open("../corpus/zhaospam_af_jieba.txt",'w')
    f.write(str)
    f.close()

if __name__ == "__main__":
    main()
