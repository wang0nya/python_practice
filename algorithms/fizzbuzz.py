def fizz_buzz(n):
    for x in n:
        if x%3 == 0:
            print('fizz', x)
        if x%5 == 0:
            print('buzz', x)
        if x%3 == 0 and x%5 == 0:
            print('fizzbuzz', x)
        else:
            print(x)

if __name__ == '__main__':
    fizz_buzz([1,2,3,4,5,6,7,8,9,10,15])