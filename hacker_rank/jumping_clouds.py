def jumping_clouds(n):
	jump, i = 0, 0
	while i<len(n)-1:
		if i+2<len(n) and n[i+2] !=1:
			i+=1
		jump+=1
		i+=1
	return jump

if __name__ == '__main__':
	n = input()
	print(jumping_clouds(n))
