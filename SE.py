n=int(input("Enter the number:"))
s=0;
for i in range(1,n+1,2):
    s+=i
print("Sum of n even numbers is :",s)


for i in range(1,n+1):
    if(i%2==0):
        s+=i
    
print("Sum of n even numbers is :",s)
