list1=['a','b','c','d']
num1=2

def generateSentence (list1,num1,str1):
    if num1==0:
        print(str1)
        return
    for element in list1:
        generateSentence(list1, num1-1 ,str1 + element)

generateSentence(list1, num1, "")