def square(n):
    '''Takes a number and returns its square.'''
    print("The square of", n, "is:", n**2)  # square of n

n = int(input("Enter a number: "))
square(n)
print(square.__doc__)
