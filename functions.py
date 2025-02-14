#Built in Library Functions
#y=max(56,78,90,23,12)
#print(y)

#x=min(56,78,90,23,12)
#print("The minimum value is", x)

#z=pow(10,30)
#print("The result value is", z)

#user-defined functions
#def greeting():
    #print("Hello World!")
#greeting()#calling a function

#def multiply():
    #num1=23
    #num2=10
   # print("The result", num1*num2)
#multiply()

#parameters(Variables) and Arguments(Values assigned to variables)
#def add(a,b):    
 #   print("The sum is", a+b)
#add(3,4)
def add(a,b):
    return a+b
a=int(input("Enter the first number: "))

b=int(input("Enter the second number: "))
print("The sum is", add(a,b))