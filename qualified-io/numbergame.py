def number_game(x, y):
    if x > y:
        return [n for n in range(y,x) if n%2==0]
    elif y==x:
        return []
    else:
        return [n for n in range(x,y) if n%2!=0]

if __name__ == '__main__':
    x = int(input())
    y = int(input())

    print(number_game(x,y))