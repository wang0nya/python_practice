def count_substring(string, sub_string):
    l_str=len(string)
    l_sub=len(sub_string)
    count=0
    for i in range(l_str-l_sub+1):
        if(string[i:i+l_sub] == sub_string ):      
            count+=1
    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)