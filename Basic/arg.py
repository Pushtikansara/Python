def average(a,b):
    #def average(a=4,b) compulsory passing of b
    print("Average is:",(a+b)/2)

average(10,20)
average(a=9,b=8)

def avg(*num):#type tuple
    sum=0
    for i in num:
     sum=sum+i
    print("Average is:",sum/len(num))

avg(10,20,30)   