def multipy(n):
    x=0
    mylist = []
    while x<10:
        x+=1
        mylist.append("{} x {} = {}".format(n,x,(x*n)))
    for x in mylist:
        print(x)
    return x

if __name__ == '__main__':
    n = int(input())
    multipy(n)