# alphabet spam problem
if __name__ == '__main__':
    N = str(input())

total = len(N)

def findWhitespace(string):
	return sum(1 for c in string if c == '_')
def findLower(string):
	return sum(1 for c in string if c.islower())
def findUpper(string):
	return sum(1 for c in string if c.isupper())
def findSymbol(string):
	return sum(1 for c in string if not c.isalpha() and c is not '_')
print(float(findWhitespace(N)/total))
print(float(findLower(N)/total))
print(float(findUpper(N)/total))
print(float(findSymbol(N)/total))
