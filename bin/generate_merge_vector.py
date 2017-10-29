

def read_file(path):
	file_list=[]
	with open(path,'r') as f:
		for line in f.readlines():
			line=line.strip()
			word_list=line.split(" ")
			file_list.append(word_list)
	return file_list

	

if __name__=='__main__':
	print ("ok")
	path_cn='../corpus/zhaospam_af_jieba.txt'
	path_py='../corpus/zhaospam_to_pinyin.txt'
	res_cn=read_file(path_cn)
	res_py=read_file(path_py)
	