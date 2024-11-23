''' Functions'''
a=10  #------------------>Global Variable
def fun(): #--------------->Defining the function
    print ("Welcome to the Fun Block")
    print("Welcome to Anudip")
    a=5  #------------------->Local Variable
    print("a=",a)

print ("First Line")
fun()   #-------------------->Calling the function  
print("a=",a)
