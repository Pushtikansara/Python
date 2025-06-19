dic = {
    "Harry": "Magician",
    "Spoon": "object"
      }
print(dic["Harry"])

Student ={
    12: "Harry",
    14: "Shivam",
    13: "Rohan",
    10: "Shivani",
    11: "Sakshi"     
}
print(Student)
#print(Student[16])# This will raise a KeyError since 16 is not a key in the dictionary
print(Student.get(16))
  # This will return None since 16 is not a key in the dictionary
print(Student.keys())# This will return all the keys in the dictionary
print(Student.values())# This will return all the values in the dictionary

for key in Student.keys():
    print(key, ":", Student[key])  # This will print each key and its corresponding value
print(Student.items())  # This will return all the key-value pairs in the dictionary