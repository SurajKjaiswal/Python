a=int(input("Enter first Number: "))
b=int(input("Enter second Number: "))
c=int(input("Enter third Number: "))
d=int(input("Enter fourth Number: "))

if(a>b and a>c and a>d):
    print("A is greater")
elif(b>c and b>d):
    print("B is greater")
elif(c>d):
    print("C is greater")
else:
    print("D is greater")
