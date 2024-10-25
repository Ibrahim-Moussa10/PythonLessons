grades = int(input("whats you're grade: "))
if grades >100 or grades <0:
    print("grades can't be more than 100 or less than 0")
elif grades >=90 :
    print('A')
elif grades >=80:
    print('B')
elif grades >=70:
    print('C')
elif grades >=60:
    print('D')
else:
    print('F')
