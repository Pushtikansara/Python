for i in range(5):
    print(i)
    if i == 3:
        print("Breaking the loop at i =", i)
        break
else:
    print("Loop completed")

i=0
while i < 5:

    print(i)
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    i += 1