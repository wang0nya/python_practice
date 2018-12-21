def main():
    i=int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    for i in arr:
        print(i, end=" ")

if __name__ == '__main__':
    main()