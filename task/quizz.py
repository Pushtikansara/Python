print("Which game is known as the father of all games?")
print("1. Chess")
print("2. Football")      #answer is 1
print("3. Cricket")
print("4. Tennis")
answer = input("Enter your answer (1-4): ")
print("What is the capital of France?")
print("1. Berlin")
print("2. London")
print("3. Paris")     #answer is 1 
print("4. Madrid")
answer2 = input("Enter your answer (1-4): ")
print("Which planet is known as the Red Planet?")
print("1. Earth")   
print("2. Mars")
print("3. Jupiter") #answer is 2
print("4. Saturn")
answer3 = input("Enter your answer (1-4): ")
print("What is the largest mammal in the world?")
print("1. Elephant")
print("2. Blue Whale")  
print("3. Giraffe") #answer is 2
print("4. Hippopotamus")
answer4 = input("Enter your answer (1-4): ")
print("What is the chemical symbol for water?")
print("1. HO2")
print("2. CO2")
print("3. H2O") #answer is 3
print("4. NaCl")
answer5 = input("Enter your answer (1-4): ")
print("What is the capital of Japan?")
print("1.Bangkok")
print("2. Seoul")
print("3. Beijing") 
print("4. Tokyo")  #answer is 4
answer6 = input("Enter your answer (1-4): ")

if answer == "1" and answer2 == "3" and answer3 == "2" and answer4 == "2" and answer5 == "3" and answer6 == "4":
    print("Congratulations! You answered all questions correctly!") 
else:
    print("Sorry, you didn't answer all questions correctly. Please try again.")
    if answer != "1":
        print("Question 1: The correct answer is 1. Chess")
    if answer2 != "3":
        print("Question 2: The correct answer is 3. Paris")
    if answer3 != "2":
        print("Question 3: The correct answer is 2. Mars")
    if answer4 != "2":
        print("Question 4: The correct answer is 2. Blue Whale")
    if answer5 != "3":
        print("Question 5: The correct answer is 3. H2O")
    if answer6 != "4":
        print("Question 6: The correct answer is 4. Tokyo")




