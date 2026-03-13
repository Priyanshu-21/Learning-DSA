# Implementation of Delete Node for Doubly Linked List 
'''
1. Delete at the Beginning: - 
    TC: - O (1)
    SC: - O (N)
2. Delete at the End 
    TC: - O(N)
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
        else:
            current = self.head
            while (current.next):
                current = current.next
            
            current.next = newNode
            newNode.prev = current
        
        return self.head

    def deleteAtBegin(self):
        current = self.head.next
        if (current):
            self.head = current

    def deleteAtEnd(self):
        current = self.head
        previous = None
        while (current.next):
            previous = current
            current = current.next
        
        previous.next = None
        current.prev = None
        
        return self.head
    
    def traverse(self):
        current = self.head 
        while (current):
            print(str(current.data) + " --> ", end=" ")
            current = current.next

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insertAtEnd(10)
    dll.insertAtEnd(20)
    dll.insertAtEnd(30)
    dll.insertAtEnd(40)
    dll.insertAtEnd(50)
    dll.insertAtEnd(60)
    dll.traverse()
    print("\n")
    dll.deleteAtBegin()
    dll.traverse()
    print("\n")
    dll.deleteAtEnd()
    dll.traverse()