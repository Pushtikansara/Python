cities={"Junagadh","Bhuj","Rajkot","Surat","Ahmedabad"}
cities2={"Somnath","Rajkot","Porbandar","Baroda","Junagadh"}
cities3=cities.union(cities2)#union method combines elements from both sets
print(cities3)

#cities.update(cities2)#update method adds elements from cities2 to cities
#print(cities)

print(cities.intersection(cities2))#intersection method returns common elements from both sets
#print(cities.intersection_update(cities2))#intersection_update method updates cities with common elements from cities2

print(cities.difference(cities2))#difference method returns elements in cities that are not in cities2

print(cities.symmetric_difference(cities2))#symmetric_difference method returns elements that are in either set but not in both

print(cities.isdisjoint(cities2))#isdisjoint method checks if there are no common elements between the two sets

print(cities.issubset(cities3))#issubset method checks if cities is a subset of cities3

print(cities.issuperset(cities2))#issuperset method checks if cities contains all elements of cities2   

print(cities3.pop())#pop method removes and returns an arbitrary element from the set

cities.add("Kutch")#add method adds a single element to the set
print(cities)

#print(cities.remove("Navsari"))#remove method removes a specific element from the set, raises KeyError if not found

cities.discard("Rajkot")#discard method removes a specific element from the set, does not raise an error if not found
print(cities)

cities.clear()#clear method removes all elements from the set
print(cities)

del cities#del statement deletes the set entirely   
#print(cities)  # This will raise an error since cities is deleted
# Uncommenting the above print statement will raise a NameError since cities no longer exists