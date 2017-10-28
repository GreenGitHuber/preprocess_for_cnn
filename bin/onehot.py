#!/usr/bin/env python
# -*- coding:utf-8 -*-
# from sklearn.preprocessing import OneHotEncoder

#fr = open('zhaospam_to_pinyin.txt','r')

#把一句话转化为拼音以后得到的string，根据是否出现某一个字母，转化为向量
def py_vec(string):
	vec_sum = [0]*26
	word_list = string.split(" ")
	for word in word_list:
		print word 
		vec = [0] *26
		for char in word:
			if char.isalpha():
				loc = ord(char)- ord('a')
			vec[loc] = 1
		print vec
		vec_sum =[a+b for a,b in zip(vec_sum,vec)]
	return vec_sum
	

if __name__=="__main__":
	vec_sum =py_vec("a b ab")
	print vec_sum
	print "hello"