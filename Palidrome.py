n=int(input("Enter a Number:"))
temp=n;
rev=0;
      
while(n!=0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("Reverse of number is",rev)
if(rev==temp):
    print("The is a Palindrome Number ")
else:
    print("The is not a Palindrome Number ")

    

