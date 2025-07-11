def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "Is a prime number.")
else:
    print(num, "Is not a prime number.")
