word = []

given = input("Enter your word: ").lower()

for element in given:
    word.append(element)

reversed_word = ''.join(word.pop() for i in range(len(word)))

if given == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")