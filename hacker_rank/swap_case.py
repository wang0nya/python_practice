def swap_case(s):
    swapped = []
    for x in s:
        if x.islower():
            swapped.append(x.upper())
        elif x.isupper():
            swapped.append(x.lower())
        else:
            swapped.append(x)
    return ''.join(swapped)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)