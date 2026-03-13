# Implementation of Delete at Begin and End at CDLL 
'''
1. Delete at begining: - 
    TC: - O (1)
    SC: - O (N)
2. Delete at End: - 
    TC: - O (N)
    SC: - O (N)
'''
class Node: 
    def __init__(self, data):
        self.prev = None 
        self.data = data 
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def insertAtBegining(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            newNode.prev = newNode.next = newNode
        else: 
            lastNode = self.head.prev
            # Update NewNode references 
            newNode.prev = lastNode
            newNode.next = self.head 

            # Update lastNode references 
            lastNode.next = newNode
            lastNode = newNode

            # Update the head 
            self.head = newNode
        
        return self.head
    
    def deleteAtBegining(self):
        lastNode = self.head.prev
        # Update the references to next Node 
        current = self.head.next
        lastNode.next = self.head.next
        current.prev = lastNode
        
        # Update references for node which we are deleting 
        self.head.next = None
        self.head = current    # Update the head to point current node 

        return self.head 
    
    def deleteAtEnd(self):
        current = self.head 
        while (current and not(current.next.next == self.head)):
            current = current.next
        
        # Delete current node references and point it to previous node ref 
        current.next.prev = None 
        current.next = self.head

        return self.head
    
    def traverse(self):
        current = self.head
        while (current):
            print(str(current.data) + " --> ", end=" ")
            current = current.next
            # Exit circular loop 
            if (current == self.head):
                break


if __name__ == "__main__":
    cdll = DoublyLinkedList()
    cdll.insertAtBegining(10)
    cdll.insertAtBegining(20)
    cdll.insertAtBegining(30)
    cdll.insertAtBegining(40)
    cdll.insertAtBegining(50)
    cdll.insertAtBegining(60)
    cdll.traverse()
    print("\n Circular Linked list after Deleting the first Node \n")
    cdll.deleteAtBegining()
    cdll.traverse()
    print("\n Circular Linked list after Deleting the Last Node \n")
    cdll.deleteAtEnd()
    cdll.traverse()

'''
Output: - 
Original Linked List 
60 -->  50 -->  40 -->  30 -->  20 -->  10 -->

Circular Linked list after Deleting the first Node (Deleted Node 50)
50 -->  40 -->  30 -->  20 -->  10 -->  

Circular Linked list after Deleting the Last Node (Deleted Node 10)
50 -->  40 -->  30 -->  20 --> 
'''