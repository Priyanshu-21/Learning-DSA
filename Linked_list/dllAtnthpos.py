# Implementation for Insert and Delete at nth position 
'''
1. Insert at nth position 
    TC: O (k) --> K is the node after which we insert the new node
    SC: O (N)
2. Delete at nth position 
    TC: O (k) --> K is the node after which we insert the new node
    SC: O (N)
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
    
    # Inesert At End 
    def insertAtNpos(self, key, data):
        newNode = Node(data)
        # Serach of the node in DLL
        current = self.head
        while (not(current == None) and not(current.data == key)):
            current = current.next

        temp = current.next
        current.next = newNode
        newNode.prev = current
        newNode.next = temp

        return self.head
    
    def deleteAtNpos(self, key):
        current = self.head
        previous = None 
        while (not(current == None) and not(current.data == key)):
            previous = current
            current = current.next
        
        nextNode = current.next

        # Change the reference of the node 
        previous.next = nextNode
        nextNode.prev = current.next

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
    print("\nInsert at nth position: - \n")
    dll.insertAtNpos(30, 35)
    dll.traverse()
    print("\nDelete at nth position: - \n")
    dll.deleteAtNpos(35)
    dll.traverse()
