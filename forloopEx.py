n=int(input("Enter the last number:"))

# first Method
for i in range(2,n+1,2):
    print(i)    

# Second method
for i in range(1,n+1):
    if(i%2==0):
        print(i,end="  ")
        
