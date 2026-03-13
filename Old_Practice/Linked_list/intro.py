# Introduction to Linked List in python 
# Insert in the beginning, in End 

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList():
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data) # Created a new node 
        if (not(self.head == None)):
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def traverse(self):
        current = self.head
        while (not current == None):
            print(str(current.data) + "-->", end=" ")
            current = current.next

if __name__ == "__main__":
    ls = singlyLinkedList()
    ls.insertAtEnd(10)
    ls.insertAtEnd(12)
    ls.insertAtEnd(21)
    ls.insertAtEnd(23)
    ls.traverse()
