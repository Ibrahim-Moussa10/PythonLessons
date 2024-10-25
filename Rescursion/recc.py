list1=['i','love','pizza']
num=3

def myFun(list1,num,str):
    if num==0:
        print(str)
        return
    for element in list1:
        myFun(list1,num-1, str+element)
print(myFun(list1,num,""))