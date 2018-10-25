#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
	N = int(input())
commandcount = 0
mylist = []
while commandcount<N:
	command = input()
	commandcount+=1
	def readcommand(i):
		func = i.partition(' ')[-3]
		value_with_index = i.partition(' ')[2]
		value_without_index = i.split(' ')[-1]
		if func == 'insert':
			index, value = value_with_index.split(' ')
			index = int(index)
			value = int(value)
			mylist.insert(index, value)
		elif func == 'remove':
			mylist.remove(int(value_without_index))
		elif func == 'append':
			mylist.append(int(value_without_index))
		elif func == 'sort':
			mylist.sort()
		elif func == 'reverse':
			mylist.reverse()
		elif func == 'pop':
			mylist.pop()
		elif func == 'print':
			print(mylist)
	readcommand(command)
