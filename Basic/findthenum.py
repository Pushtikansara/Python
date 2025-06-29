n = int(input())     # How many numbers?
a = []               # Create an empty list

# Take input numbers one by one
for i in range(n):
    num = int(input())
    a.append(num)

# Go through each number
for i in a:
    if a.count(i) == 1:    # Count how many times this number appears
        print(i, end=' ')
