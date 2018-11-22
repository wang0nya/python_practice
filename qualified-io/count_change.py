def count_change(money,coins):
	if money == 0:
		return 1
	elif money<0 or len(coins)==0:
		return 0
	else:
		coin = coins[-1]
		return sum(
				count_change(i, coins[:-1])
				for i in range(money, -1, -coin))
	
if __name__ == '__main__':
	print(count_change(4, [1,2]))