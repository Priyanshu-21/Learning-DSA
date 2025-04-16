# Implementation on how to delete node at begining or at end 
class Node: 
    def __init__(self, data):
        self.data =  data
        self.next = None

class LinkedList:
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
        
        return self.head
    
    def deleteNodeAtBegin(self):
        current = self.head 
        self.head = current.next

        return self.head

    def deleteAtEnd(self):
        current = self.head
        prev = None
        while (current.next):
            prev = current
            current = current.next
        
        # Delete at end logic 
        prev.next = None

        return self.head
    

    def traverse(self):
        current = self.head
        while (not(current == None)):
            print(str(current.data) + " --> ", end=" ")
            current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtEnd(10)
    ll.insertAtEnd(20)
    ll.insertAtEnd(30)
    ll.insertAtEnd(40)
    ll.traverse()
    # Delete Node at Beginning 
    ll.deleteNodeAtBegin()
    print("\n")
    ll.traverse()
    # Delete Node at End 
    ll.deleteAtEnd()
    print("\n")
    ll.traverse()

    