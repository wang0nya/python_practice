def rstring(n, string):
    return (string.count("a") * (n // len(string)) + string[:n % len(string)].count("a"))

if __name__ == '__main__':
    string=input()   
    n=int(input())
    print(rstring(n, string))
