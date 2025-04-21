# Implementation of Circular Linked List 
'''
1. Insert at Begining: - 

'''
class Node: 
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None 

class CircularLinkedList: 
    def __init__(self):
        self.head = None 

    def insertAtBegin(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else: 
            # Wrong Implementation of circular Linked List need to check on this 
            current = self.head
            curHead = self.head
            while (current == None):
                current = current.next
                if (current == self.head):
                    exit
            
            self.head = newNode
            newNode.next = curHead
            curHead.prev = newNode
            current.next = self.head 

        return self.head
    
    def traverse(self):
        slow = self.head
        while (slow):
            print(str(slow.data) + " --> ", end=" ")
            slow = slow.next

if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insertAtBegin(10)
    cll.insertAtBegin(5)
    cll.insertAtBegin(15)
    cll.traverse()