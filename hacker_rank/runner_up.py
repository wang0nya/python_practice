if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = list(dict.fromkeys(arr))

#if len(mylist) == n:
print(sorted(mylist, reverse=True)[1])