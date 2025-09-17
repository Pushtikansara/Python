
i=0
for i in range(5):
    str = input("enter a String:")
    str1 = str[::-1]
    if(str1==str):
        print("Both are equal")
    else:
        print("Different")
