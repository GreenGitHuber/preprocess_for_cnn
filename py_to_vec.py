def py_vec(string):
	vec = [0] *26
	lenth = len(string)
	for char in string:
    		if char.isalpha():
				loc = ord(char)- ord('a')
				vec[loc] = 1
	return vec
	

if __name__=="__main__":
	vec =py_vec(" \n ")
	print vec
	print "hello"