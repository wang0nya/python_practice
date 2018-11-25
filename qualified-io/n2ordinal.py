def ordinal(value):
    if value % 100//10 != 1: # check to avoid values like 111 => 111st, 112 => 112nd
        if value % 10 == 1:
            ordval = "%d%s" % (value, "st")
        elif value % 10 == 2:
            ordval = "%d%s" % (value, "nd")
        elif value % 10 == 3:
            ordval = "%d%s" % (value, "rd")
        else:
            ordval = "%d%s" % (value, "th")
    else:
        ordval = "%d%s" % (value, "th") # 111 => 111th, 112 => 112th

    return ordval

if __name__ == '__main__':
    value = int(input())
    print(ordinal(value))
