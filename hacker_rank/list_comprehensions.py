# list comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
mylist = [] 
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a + b + c != n:
                mylist.append([a,b,c])
print(mylist)