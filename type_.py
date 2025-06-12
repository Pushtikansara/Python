student = {
    "name": "Pushti",
    "age": 18,
    "course": "Python"
}
print(student)

colour=["Red", "Green", "Blue"]
print(colour)

#print(colour[0]="Pink")  # This line will raise a SyntaxError
# Correcting the above line to change the first element of the list 

colour[0] = "Pink"
print(colour)
if "Pink"in colour:
    print("Pink is in the list")

tup=(2,1,"hello",True,3.14)
print(tup)
print(tup[0])#we can not change the value of tuple
tup1=tup[0:3]
print(tup1)

print("=======================================================")

print(type(student))  # <class 'dict'>
print(type(colour))   # <class 'list'>      
print(type(tup))      # <class 'tuple'>