word = ("yft uf  kg ufyfk fiy dif")

word_list = word.split()

intt1 = int(input("yfyuf"))

intt2 = int(input("yfyuf"))

if 0 <= intt1 < intt2 <= len(word_list):

    word_slice = word_list[intt1:intt2]

    print(f"tdy{word_slice}")

else:
    
    print("in") 