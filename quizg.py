questions = (("whats my name?"), 
             ("whats my age?"), 
             ("whats my height?"))

options = (("A. Ali", "B. Mohammad", "C. Ibrahim"),
           ("A. 24", "B. 50", "C. 40"),
           ("A. 155cm", "B. 120cm", "C. 176cm"))


answers = ("C", "A", "C")
guesses = []
score = 0
question_number = 0

for quetion in questions:
    print ("-------------------")
    print (quetion)
    for option in options [question_number]:
        print (option)
    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print ("Your right!")
    else:
        print ("You are wrong!")
        print(f"{answers[question_number]} is the correct answer")
    question_number += 1

print("--------------------------")
print("         RESAULTS         ")
print("--------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score = score / len(questions) * 100
score = int(score)
print(f"You scored {score}%")

# quiz = [["whats my name?", ["Ali", "Mohammad", "Ibrahim"], 2],
#         ["How old I am?", ["23", "24", "-1"], 0]]


# for i in quiz:
#     print(i[0])

#     for j in range(len(i[1])):
#         print(f'{j}. {i[1][j]}')

#     ans = int(input())
#     if ans != i[2]:
#         print('Wrong answer bitch')
#         break
#     print("correct")


