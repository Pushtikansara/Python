letter= "My name is {} and I am {} years old. I live in {}."
name="Pushti"
age='18'
city="Anand"
print(letter.format(name, age, city))

txt="Bank balance is {price:.2f} rupees."
print(txt.format(price= 123456.56789)) # Using format with positional and keyword arguments

print(f"My name is {name} and I am {age} years old. I live in {city}.")# Using f-string for formatting

print("My name is {{name}} and I am {{age}} years old. I live in {{city}}.")