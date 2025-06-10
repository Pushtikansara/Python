def comparison(a,b):
    if(a>b):
        print("a is greater than b")
    elif(a==b):
        print("a is equal to b")
    else:
        print("a is less than b")

def addition(a,b):
    print("The sum of a and b is:",a+b) 
def subtraction(a,b): 
    print("The difference of a and b is:",a-b) 
def multiplication(a,b): 
    print("The product of a and b is:",a*b)
def division(a,b):
    if b != 0:
        print("The division of a and b is:",a/b)
    else:
        print("Division by zero is not allowed")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
comparison(a,b)      
addition(a,b) 
subtraction(a,b)
multiplication(a,b)         
division(a,b)