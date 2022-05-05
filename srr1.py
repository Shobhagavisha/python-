from ctypes.wintypes import HGDIOBJ


x =input("enter the string")

def show(string_1):
    count1 = 0
    count2 = 0
    for i in string_1:
        if(i.islower()):
            count1=count1+1
        elif(i.isupper()):
             count2=count2+1  
    print("the number of lowercase character is", count1)
    print("the number of upper case letters is:", count2)  

show(x)



#length of a string
str_len="welcome to python programming"
print("string length of:",len(str_len))

#number of character
def num(str):
    count=dict()
    char=str
    for ch in char:
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    return count     

print(num("sdcsfffdgshfggg"))


#to get a string
 
def get(str):
    if(len(str)<3):
        print(str[0:1])
    elif(len(str)>5):
        print(str[0:2]+str[-2:])
    else:
        print(str*2)        
get("asdf")



    
 
