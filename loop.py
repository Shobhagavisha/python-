n=int(input("enter n value"))
for i in range(n):
    print("B"*i)


n=int(input("enter n value"))
for i in range(n):
    print("B"*(n-i)) 

n=int(input("enter n value"))

for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print(" ")    


