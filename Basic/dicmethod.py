Student1 = {
    12: "Harry",
    14: "Shivam",
    13: "Rohan",
     
}
Student2 ={
    10: "Shivani",
    11: "Sakshi"    }
Student1.update(Student2)  # This will merge Student2 into Student1
print(Student1)  # This will print the updated dictionary with all key-value pairs
#Student1.clear() # This will remove all key-value pairs from the dictionary
#print(Student1)  # This will print an empty dictionary since all key-value pairs have been removed
empty_dict = {}  # This will create an empty dictionary
print(empty_dict)  # This will print an empty dictionary
Student2.pop(10)  # This will remove the key-value pair with key 10 from Student2
print(Student2)  # This will print the updated dictionary with the key-value pair removed 
Student1.popitem()  # This will remove the last inserted key-value pair from Student1  
print(Student1)
del Student1[12]  # This will delete the key-value pair with key 12 from Student1
print(Student1)  # This will print the updated dictionary with the key-value pair removed   
#del Student1["12"]  # This will raise a KeyError since "12" is not a key in the dictionary