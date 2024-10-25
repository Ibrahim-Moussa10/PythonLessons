class Node:
    def __init__ (self,info,n=None):
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
            self.size=+1
        else:
            n=Node(val,None)
            self.tail.next=n
            self.tail=n
            self.size+=1

    def deleteHead(self):
        if self.size==0:
            return None
        if self.size==1:
            val=self.head.info
            self.head=None
            self.tail=None
            self.size-=1
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
            while temp.next != self.tail:
                temp=temp.next
            self.tail=temp
            self.tail.next=None
            self.size-=1
            return val
        
    def search(self,target):
        current = self.head
        while current != None:
            if current.info== target:
                return current
            current = current.next
        return None

    def printLL(self):
        temp=self.head
        while temp!=None:
            print(temp.info,"->" ,end="")
            temp=temp.next
        print()
ll=LinkedList()

ll.addToHead(12)
ll.printLL()
ll.addToHead(24)
ll.printLL()
ll.addToTail(5)
ll.printLL()
ll.addToTail(8)
ll.printLL()
ll.addToTail(9)
ll.printLL()
ll.addToTail(16)
ll.printLL()
ll.addToTail(7)
ll.printLL()
ll.addToTail(5)
ll.printLL()

ll.deleteTail()
ll.printLL()
ll.deleteHead()

result = ll.search(16)
if result:
    print(f"Found: {result.info}")

else:
    print("Not Found")


