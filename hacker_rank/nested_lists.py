#Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
from collections import Counter

if __name__ == '__main__':
    mylist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([name, score])

# sort the lists using second element  
# of sublist Function to sort using sorted() 
def Sort(mylist): 
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    mysortedlist = sorted(mylist, key = lambda x: x[1])

    # [1] to skip the lowest and go to second lowest
    secondlowest = mysortedlist[1]

    # check for duplicates
    counts = Counter(tuple(mysortedlist))
    output = [value for value, count in counts.items() if count > 1]
    print(output)

    return(secondlowest)

myvalue_name = Sort(mylist)[0]
myvalue_score = Sort(mylist)[1]
print(myvalue_name)
print(myvalue_score)