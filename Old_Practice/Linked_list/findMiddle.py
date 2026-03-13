# Find Middle element in linked list 
import math
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        newNode = Node(data)
        if (not(self.head == None)):
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            self.head = newNode
    
    def findMiddle(self):
        current = self.head 
        temp = current.next
        count = 0
        while temp.next:
            count = count + 1
            temp = temp.next
        
        middle = math.floor((count + 1) / 2)
        return middle
    
    def insertAtMiddle(self, data, value):
        newNode = Node(value)
        current = self.head
        while not(data == 0):
            current = current.next
            data = data - 1
        # Need to implement the insert at middle logic here 
        temp = current.next
        current.next = newNode
        newNode.next = temp

    def traversal(self):
        current = self.head
        while current:
            print(str(current.data) + " ---> ", end=" ")
            current = current.next
        

if __name__ == "__main__":
    ll = linkedList() # Created object
    ll.insertAtBegin(10)
    ll.insertAtBegin(20)
    ll.insertAtBegin(30)
    ll.insertAtBegin(40)
    ll.insertAtBegin(50)
    middle = ll.findMiddle()
    ll.insertAtMiddle(middle, 25)
    ll.traversal()
