# Implementation of Circular Linked List 
'''
1. Insert at Begining: - 
    TC: O (N)
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
    
    def insertAtBegin(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            newNode.prev = newNode.next = self.head 
        else:
            lastNode = self.head.prev
            # update the previous & next point refrences 
            newNode.next = self.head 
            newNode.prev = lastNode
            # update the last node previous & next point refrences 
            self.head.prev = newNode
            lastNode.next = newNode  # key point to make DLL circular 

            self.head = newNode


        return self.head
    
    def traverse(self):
        current = self.head 
        while (current):
            print(str(current.data) + " --> ", end=" ")
            current = current.next
            


if __name__ == "__main__":
    cll = DoublyLinkedList()
    cll.insertAtBegin(10)
    cll.insertAtBegin(20)
    cll.insertAtBegin(30)
    cll.traverse()