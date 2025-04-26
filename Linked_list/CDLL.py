# Implementation on Insert & Delete Node at nth position 
'''
1. Insert at Nth Position: - 
    TC: - O(K) --> search the key k an then insert it after the node search 
    SC: - O(N)

2. Delete at Nth Position: - 
    TC: - O(K) --> Seach the key in linked list & delete the searched node 
    SC: - O(N)
'''

class Node: 
    def __init__(self, data):
        self.prev = None 
        self.data = data 
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 
    
    def insertAtEnd(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            newNode.prev = newNode.next = newNode
        else: 
            current = self.head 
            while (current and not(current.next == self.head)):
                current = current.next
            
            # Update the reference of newNode 
            newNode.next = self.head
            newNode.prev = current

            # Update the prev last node references 
            current.next = newNode
            self.head.prev = newNode

        return self.head
    
    def insertAtNPos(self, key, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            newNode.prev = newNode.next = newNode
        else: 
            current = self.head 
            while (current and not(current.data == key)):
                current = current.next 
            
            # Now we need to insert node after matched Node 
            # Update references of NewNode 
            newNode.prev = current
            newNode.next = current.next 
            # Update references of current & current old next 
            current.next.prev = newNode
            current.next = newNode
        
        return self.head 
    
    def deleteAtNPos(self, key):
        if (self.head.data == key):
            # Deleting the first Node of LinkedList 
            self.head.next.prev = self.head.prev 
            self.head.prev.next = self.head.next

            self.head = self.head.next 
            return self.head
        
        current = self.head 
        while (current and not(current.data == key)):
            current = current.next

        # Update current node adjacent nodes references 
        current.prev.next = current.next 
        current.next.prev = current.prev 

        # Update current node references  
        current.prev = current.next = None 

        return self.head 
    
    def traverse(self):
        current = self.head 
        while (current):
            print(str(current.data) + " --> ", end=" ")
            current = current.next
            if (current == self.head):
                break


if __name__ == "__main__":
    cdll = DoublyLinkedList()
    cdll.insertAtEnd(10)
    cdll.insertAtEnd(20)
    cdll.insertAtEnd(30)
    cdll.insertAtEnd(40)
    cdll.insertAtEnd(50)
    cdll.insertAtEnd(60)
    cdll.insertAtEnd(70)
    cdll.traverse()
    print("\n Insert Node at nth postion \n")
    cdll.insertAtNPos(10, 45)
    cdll.traverse()
    print("\n Delete node at nth postion \n")
    cdll.deleteAtNPos(30)
    cdll.traverse()

'''
Output Expected: - 
Original Linked List 
10 -->  20 -->  30 -->  40 -->  50 -->  60 -->  70 -->  

Insert Node at nth postion 
10 -->  45 -->  20 -->  30 -->  40 -->  50 -->  60 -->  70 -->  

Delete node at nth postion 
10 -->  45 -->  20 -->  40 -->  50 -->  60 -->  70 -->

Corner Cases: - Delete at End & Begining (Done) | Insert at End & Begining (Done)
'''