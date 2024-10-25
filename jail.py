jail=input("Did you kill somone? y/n: ")
theif=input("Did you steal anything? y/n: ")
drunk=input("Are you drunk? y/n: ")
driving=input("were you driving? y/n: ")

if jail == "y" or theif == "y" or ( driving == "y" and drunk == "y"):

    print("Go to jail")
else :
    print ("You'r free")