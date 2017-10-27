from sklearn.preprocessing import OneHotEncoder

#fr = open('zhaospam_to_pinyin.txt','r')
def py_vec(string):
	vec = [0] *26
	lenth = len(string)
	for char in string:
		loc = char - 'a'
	vec[loc] = 1
	return vec
	

if __name__=="__main__":
	vec =py_vec("ab")
	print (vec)
	print ("hello")
