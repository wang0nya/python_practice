def digitize(n):
	if n>0:
		result = [int(i) for i in str(n)]
		return result
	else:
		return []

if __name__ == '__main__':
	n = int(input())
	print(digitize(n))