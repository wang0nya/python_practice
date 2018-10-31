def split_and_join(line):
    mystring = []
    for x in line:
        mystring.append(x)
        repl = [x.replace(' ', '-') for x in mystring]
    return ''.join(repl)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)