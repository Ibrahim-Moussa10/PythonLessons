#Ex : 1
# word = []

# given = input("Enter your word: ").lower()

# for element in given:
#     word.append(element)

# reversed_word = ''.join(word.pop() for i in range(len(word)))

# if given == reversed_word:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Ex : 2

# def is_balanced (expression):
#     stack=[]
#     matching_brackets = {')': '(', '}': '{', ']': '['}
#     for brackets in expression:
#         if brackets in matching_brackets.values():
#             stack.append(brackets)
#         elif brackets in matching_brackets.keys():
#             if not stack or stack[-1] != matching_brackets[brackets]:
#                 return False
#             stack.pop()
#     return len(stack) == 0
# print(is_balanced("(1+2)-3*[41+6]"))
# print(is_balanced("(1+2)-3*[41+6}"))
# print(is_balanced("(1+2)-3*[41+6"))
# print(is_balanced("(1+2)-3*]41+6["))
# print(is_balanced("(1+[2-3]*4{41+6})"))

#Ex : 3

def decode_messages(message):
    stack = []

    for element in message:
        if element in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ':
            stack.append(element)
        elif element == '*':
            if stack:
                stack.pop()

    while stack:
        stack.pop()

    return ''.join(stack).strip()

input = "SIVLE ****** DAED TNSI ***"

print(decode_messages(input)) 