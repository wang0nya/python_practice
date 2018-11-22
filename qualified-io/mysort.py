def my_sort(n):
	n.sort(key=lambda v: (v%2==0, v))
	return n

if __name__ == '__main__':
	n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print(my_sort(n))