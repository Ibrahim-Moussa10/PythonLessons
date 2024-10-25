#Question_1

list1 = [54,76,2,4,98,100]
int1=int(input("Give int1: "))
int2=int(input("Give int2: "))

print("The range value of given int is: ")


if int1 > int2 :
    print("Error: int1 should be less than or equal to int2.")
else:
    for num in list1:
        if int1 <= num <= int2:
            print(num)
#-------------------------------------------------------------------------------------
#Question_2

names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
while True:
    letter= input("Give a letter to check (quit to quit): ")
    if letter.lower() == 'quit':
        break
    found = False
    for name in names:
        if letter.lower() in name.lower():
            print(name)
            found = True
    if not found:
        print("No name contain the letter you gave")
#-------------------------------------------------------------------------------------
# #Question_3
numbers = [-12, 4, 12, 25, 67]
while True:
    
    added_number = int(input("Add a number (-99 to quit): "))
    if added_number == -99:
        break
    numbers.append(added_number)
    numbers.sort()
    print(numbers)
# #-------------------------------------------------------------------------------------
# #Question_4

words = "Is this the real life? Is this just fantasy? Caught in a landslide,no escape from reality Open your eyes, look up to the skies and see Im justa poor boy, I need no sympathy Because Im easy come, easy go, little high,little low Any way the wind blows doesnt really matter to me, to me Mama,just killed a man Put a gun against his head, pulled my trigger, now hesdead Mama, life had just begun But now Ive gone and thrown it all away Mama,ooh, didnt mean to make you cry If Im not back again this time tomorrowCarry on, carry on as if nothing really matters Too late, my time has comeSends shivers down my spine, bodys aching all the time Goodbye, everybody,Ive got to go Gotta leave you all behind and face the truth Mama, ooh (anyway the wind blows) I dont wanna die I sometimes wish Id never been born atall I see a little silhouetto of a man Scaramouche, Scaramouche, will you dothe Fandango? Thunderbolt and lightning, very, very frightening me (Galileo)Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But Im just a poorboy, nobody loves me Hes just a poor boy from a poor family Spare him hislife from this monstrosity."

intt1=int(input("Enter int1: "))
intt2=int(input("Enter int2: "))

if intt2 > 1129:
    intt2 == 1129

sliced_words = words[intt1:intt2]

print(f"Your piece is: '{sliced_words}'")
# #-------------------------------------------------------------------------------------