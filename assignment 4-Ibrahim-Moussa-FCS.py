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

# def decode_message(message):
#     stack = []
#     current_word = ""
    
#     for char in message:
#         if char == '*':
#             if current_word:
#                 stack.append(current_word)
#                 current_word = ""
#         else:
#             current_word += char
            
#     if current_word:
#         stack.append(current_word)

#     return ' '.join(reversed(stack))

# message = "SIVLE ****** DAED TNSI ***"
# decoded = decode_message(message[::-1])
# print(decoded)

#Ex : 4
class Node:
    def __init__(self, info, n=None):
        self.info = info
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addToHead(self, val):
        if self.size == 0:
            n = Node(val)
            self.head = n
            self.tail = n
        else:
            n = Node(val, self.head)
            self.head = n
        self.size += 1

    def addToTail(self, val):
        if self.size == 0:
            n = Node(val)
            self.head = n
            self.tail = n
        else:
            n = Node(val)
            self.tail.next = n
            self.tail = n
        self.size += 1

    def deleteAtLocation(self, location):
        if self.size==0:
            return None

        if location == 0:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return

        current = self.head
        previous = None
        count = 0

        while current and count < location:
            previous = current
            current = current.next
            count += 1

        if current is None:
            return None

        previous.next = current.next
        if previous.next is None:
            self.tail = previous
        self.size -= 1

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.info, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.addToHead(12)
ll.addToHead(56)
ll.addToHead(76)
ll.addToHead(11)
ll.addToHead(0)

ll.printLL()

ll.deleteAtLocation(0)
ll.printLL()

ll.deleteAtLocation(2)
ll.printLL()

ll.deleteAtLocation(0)
ll.printLL()