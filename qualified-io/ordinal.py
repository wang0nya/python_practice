import math
def numbertoordinal(number):
	if number != 0:
		ordinal = lambda number: '%d%s' % (number, 'tsnrhtdd'[(math.floor(number/10)%10!=1)*(number%10<4)*number%10::4])
	
		return ordinal(number)

print(numbertoordinal(0))