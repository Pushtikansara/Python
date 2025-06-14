lst=[1,4,5,"Joy",True,3.12]
print(lst)
print(len(lst))
print(lst[5])
print(lst[-3])
print(lst[3:5])
if "1"in lst:
    print("1 is in the list")
else:
    print("1 is not in the list")#beacause 1 is in the "" so considered as string

if 1 in lst:
    print("1 is in the list")
else:
    print("1 is not in the list")
if "o" in "Joy":
    print("o is in the string")
else:
    print("o is not in the string")
print("=======================================================")
print("=======================================================")   
a="list comprehension"
print(a.center(50,"*"))
num=[i for i in range(1,15)]
print(num)
num1=[i for i in range(1,15) if i%2==0]
print(num1)