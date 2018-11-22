def power(a,b):
	if(b==1):
		return a
	else:
		return (a*power(a,b-1))
	
if __name__ == '__main__':
	a = int(input()) # base
	b = int(input()) # raise
	
	print(power(a,b))