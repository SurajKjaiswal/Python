n=int(input("Enter a year: "))
if(n%4==0)and (n%100!=0):
    print(n,"is a Leap year.")
elif(n%400) and (n%100==0):
    print(n,"is a Leap year.")
else:
    print(n,"is not a Leap year.")
    


    

#<-------- Output -------->
'''
Enter your year: 2025
2025 is not a Leap year.

Enter your year: 2024
2024 is a Leap year.

'''
