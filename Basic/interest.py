class Interest:
    def __init__(self):
        self.principal = 0
        self.rate = 0
        self.time = 0

    def interest(self):
        return self.principal * self.rate * self.time / 100.0


class Compare:
    @staticmethod
    def compare(a, b):
        return a if a > b else b


# Main logic
i = Interest()

# First set of values
i.principal = 1000
i.rate = 5
i.time = 2
result1 = i.interest()
print("The interest of first values:", result1)

# Second set of values
i.principal = 5000
i.rate = 15
i.time = 2
result2 = i.interest()
print("The interest of second values:", result2)

# Compare the two results
greater = Compare.compare(result1, result2)
print("The greater interest is:", greater)
