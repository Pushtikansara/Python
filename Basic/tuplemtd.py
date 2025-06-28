tup = (1, 2, 5, "hello", True, 3.14)
print(tup)

#we can not use different methods on tuple like we use in list

countries=("India", "USA", "Canada", "Australia")
countries1=("Italy", "China", "Japan")
# Concatenating tuples
all_countries = countries + countries1
print(all_countries)
print(len(all_countries))

meth=list(all_countries)
if "India" in meth:
    print("India is in the list of countries")

meth.append("Germany")
print(meth)
#meth.reverse("Chaina")
print(meth)
meth.pop(5)

if "ralia" in meth:
    meth.replace("ralia","ria")
    print(meth)

tup2=(1,2,5,3,6,7,8,2,4,6,1,4)
temp=list(tup2)
temp.sort()
print(temp)
temp.index(2,3,8)
#find 2 between index 3 and 8
print(temp)
