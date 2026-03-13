# Implementation of doubly Linked List 
'''
1. Insert Opration: Insert at Beginning 
    TC: - O (1)
    SC: - O (N)
2. Insert Operation: Insert at end 
    TC: - O (N) {Need to traverse through dll and make the pointer be at end Node}
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
    
    def insertAtBegin(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

        return self.head 
    
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
    
    def traverse(self):
        current = self.head
        while (current):
            print(str(current.data) + " ---> ", end=" ")
            current = current.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insertAtBegin(10)
    dll.insertAtBegin(20)
    dll.insertAtBegin(30)
    dll.traverse()
    print("\n")
    dll.insertAtEnd(40)
    dll.insertAtEnd(50)
    dll.insertAtEnd(60)
    print("Inert at End: -- ", end="\n")
    dll.traverse()