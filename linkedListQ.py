class Node:
    def __init__(self,info,n):
        self.info=info
        self.next=n

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def addToHead(self,val):
        if self.size==0:
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,self.head)
            self.head=n
            self.size+=1
            
    def addToTail(self,val):
        if self.size==0:
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,None)
            self.tail.next=n
            self.tail=n
            
            self.size+=1
            
    def deleteHead(self):
        if self.size==0:
            return 
        if self.size==1:
            val=self.head.info
            self.head=None
            self.tail=None
            self.size=0
            return val
        
        else:
            val=self.head.info
            self.head=self.head.next
            self.size-=1
            return val
    
    def deleteTail(self):
        if self.size<=1:
            return self.deleteHead()
        else:
            val=self.tail.info
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            self.tail=temp
            self.tail.next=None
            
            self.size-=1
            return val
    def printLL(self):
        temp=self.head
        while temp!=None:
            print(temp.info," -> ",end=" ")
            temp=temp.next
        print()
        
    def addToIndex(self,info,index):
        pass

class Queue:
    def __init__(self):
        self.elements=LinkedList()
    
    def enqueue(self,val):
        self.elements.addToTail(val)
    
    def dequeue(self):
        return self.elements.deleteHead()
    
class Stack:
    def __init__(self):
        self.elements=[]
    def push(self,val):
        self.elements.append(val)
    def pop(self):
        if len(self.elements)==0:
            return None
        return self.elements.pop()

s=Stack()
q=Queue()

for i in range(4):
    q.enqueue(i)
    s.push(i)
    
for i in range(5):
    print(q.dequeue(),end=" ")
print()    
for i in range(5):
    print(s.pop(),end=" ")
print()

class MinPQ:
    def __init__(self):
        self.elements=[]
    
    def add(self,val):
        self.elements.append(val)
        
    def delete(self):
        if len(self.elements.index)==0:
            return None
        minIndex=0
        for i in range(len(self.elements)):
            if self.elements[i]<self.elements[minIndex]:
                minIndex=i
        return self.elements.pop(minIndex)