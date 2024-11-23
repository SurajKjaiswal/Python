''' find the grade of student
    find total
    find average
    grade >=90 a
    >=70   b
    >=50   c
    >=40   pass
    <40 Fail
    '''
name=input("Enter your name")
s1=int(input("Enter Your Marks of S1:"))
s2=int(input("Enter Your Marks of S2:"))
s3=int(input("Enter Your Marks of S3:"))

Total=s1+s2+s3

print("Total marks of",name,"is:",Total)

Average=Total/3
print("Average Marks of",name,"is:",Average)
if(Average>=90):
     print("Grade of ",name, "is A")
elif(Average>=70):
    print("Grade of ",name ,"is B")
elif(Average>=50):
    print("Grade of ",name ,"is C")
elif(Average>=40):
    print(name ,"is Pass")
else:
    print(name ,"is Fail")
