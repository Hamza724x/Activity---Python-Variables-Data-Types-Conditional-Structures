# # # Python Variables, Data Types, Conditional Structures
# # Problem Statement:
# # Create a Python program that asks the user three simple questions. The program will track the user's score and display the results at the end.

score = 0

print("Welcome to the quiz game. You will have to correctly answer 3 simple questions.\n")

print("Question 1 \n")
q1 = input("What is the capital of England? ")

if q1 == "london" or q1 == "London":
    print(q1 + " is the correct answer")
    score += 1;
else:
    print(q1 + " Is the wrong answer")

print("Question 2 \n")
q2 = input("Which country won the 2010 World cup? ")

if q2 == "Brazil" or q2 == "brazil":
    print(q2 + " is the correct answer")
    score += 1;
else:
    print(q2 + " Is the wrong answer")

print("Question 3 - Last question\n")
q3 = input("Is manchester blue or red? ")

if q3 == "Red" or q3 == "red":
    print(q3 + " is the correct answer")
    score += 1;
else:
    print("Wrong. Manchester will always be red because Manchester United is better than Manchester City. It would never be " + q3)
    

print("\nYour final score is " + str(score))

if score == 3:
    print("\nYou excelled at this quiz game")
elif score == 2:
    print("\nYou did great at this quiz game")
elif score == 1:
    print("\nYou did ok at this quiz game. Keep trying")
else:
    print("\nYou got 0 score because you don't support Manchester United.")

print("Goodbye!")