def main():
    i=int(input())
    s=[]
    while len(s) < i:
        a=input()
        s.append(a)

    """General syntax of string slicing is string[start:end:jump] where:
        start: is the starting index for slicing the string. Empty value means start of the string i.e. index 0
        end: is the index till which you want to slice the string. Empty value means end of the string
        jump: is used to jump the elements from start such that you'll get values in the order start, start+jump, start+2*jump, so on till your string reaches end. Empty value means 1"""

    for x in s:
        odd=x[1::2]
        even=x[::2]
        print(even, odd)

if __name__ == "__main__":
    main()