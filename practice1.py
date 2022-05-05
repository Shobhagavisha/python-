
def count_char(str):
    count=dict()
    characters=str
    for character in characters:
        if character in count:
            count[character]+=1
        else:
            count[character]=1
    return count 
print(count_char("abbcccsssddaddf"))


str1=input("enter a string")
def count_ch(str1):

    count={} 
    for each_item in str1:
    
        if each_item  in count:
            count[each_item]+=1 
        else:
            count[each_item]=1
    return count    
print(count_ch(str1))    
