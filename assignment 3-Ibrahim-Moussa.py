# #E1
def binarySearch(arr,l,h,key):
    if l > h:
        return False
    mid = (l + h)  //2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return binarySearch(arr,mid+1,h,key)
    else:
        return binarySearch(arr,l, mid-1,key)


arr = [1,2,3,4,5,6,7,8,9]
print(binarySearch(arr,0,len(arr)-1,1))

# #E2

list1=['a','b','c']
num=2

def myFun(list1,num,str):
    if num==0:
        print(str)
        return
    for element in list1:
        myFun(list1,num-1, str+element)
print(myFun(list1,num,""))

#E3 Adding a number to a sorted list

list1=[1,34,56,78,89]
nm=int(input("Add a number: "))

insert = False

for i in range (len(list1)):
    if nm < list1[i]:
        list1.insert(i, nm)
        insert = True
        break

if not insert:
    list1.append(nm)

print(list1)

#E4 POS for aamo el dekanje

class Item:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price

class POS:
    def __init__(self):
        self.items = {}
        self.load_items()
    
    def load_items(self):
        
        self.items['1111'] = Item('1111', 'Batata', 0.7)
        self.items['2222'] = Item('2222', 'Bezer', 0.3)
        self.items['3333'] = Item('3333', 'Indomie', 0.5)
        self.items['4444'] = Item('4444', 'chocolate', 1)

    def start_receipt(self):
        total_cost = 0
        receipt_items = []
        
        while True:
            barcode = input("Enter item barcode: ")
            quantity = int(input("Enter quantity: "))
            
            if barcode in self.items:
                item = self.items[barcode]
                cost = item.price * quantity
                total_cost += cost
                receipt_items.append((item.name, quantity, item.price, cost))
                print(f"Added {quantity} * {item.name} to the receipt.")
            else:
                print("Item not found. Please enter a valid barcode.")

            another_item = input("Would you like to add another item? (y/n): ").strip().lower()
            if another_item != 'y':
                break
        
        self.print_receipt(receipt_items, total_cost)

    def print_receipt(self, receipt_items, total_cost):
        print("\nReceipt:")
        for name, quantity, price, cost in receipt_items:
            print(f"item: {name} ({quantity}) x {price:.2f}$ = {cost:.2f}$")
        print(f"Total Amount: ${total_cost:.2f}\n")

    def run(self):
        while True:
            start_new_receipt = input("Would you like to start a new receipt? (y/n): ").strip().lower()
            if start_new_receipt == 'y':
                self.start_receipt()
            else:
                print("Thank you for using the POS. Goodbye!")
                break

if __name__ == "__main__":
    pos_system = POS()
    pos_system.run()