a=10  #-----------> Declaring Global Variable
def fun():
    a=5  #---------> Declaring Local Variable
    print("Local Variable")
    print("Value of a is: " , a)#-----> Print Local vriable
    
print("Global Variable")
print("Value of a is:",a)  #--------> Print Global Variable
fun()    #---------> Calling Function



#<--------------------- Output -------------------->
    
