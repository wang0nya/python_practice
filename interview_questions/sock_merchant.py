#return an integer representing the number 
#of matching pairs of socks that are available.

def sockMerchant(n, ar):
    d = { x:ar.count(x) for x in ar }
    pairs = 0
    for _, value in d.items():
        pairs += value//2
    return pairs

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = print(sockMerchant(n, ar))