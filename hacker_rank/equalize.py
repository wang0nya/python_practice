def equalizeArray(arr):
    d={x:arr.count(x) for x in set(arr)}
    values=list(d.values())
    unique=max(values)
    remove_unique=values.remove(2)
    return remove_unique

if __name__ == '__main__':
    arr=list(map(int, input().rstrip().split()))
    print(equalizeArray(arr))