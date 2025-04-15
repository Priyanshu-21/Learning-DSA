# Implementation of Deletion & Insertion of element in Singly Linked List at nth Position
'''
1. Delete node at nth position 
- Searching the linked list till nth position 
- prev counter takes values of previous node 
- prev.next = current.next (when node is found in linked list)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else: 
            temp = self.head
            self.head = newNode
            newNode.next = temp
        
        return self.head
    
    def delete(self, k):
        curr = self.head
        prev = None
        while (not(curr == None) and not(curr.data == k)):
            prev = curr
            curr = curr.next

        prev.next = curr.next # This condition fails to delete node at 1st Position

        return self.head

    def traverse(self):
        current = self.head
        while (not(current == None)):
            print(str(current.data) + " --> ",end=" ")
            current = current.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegin(50)
    ll.insertAtBegin(20)
    ll.insertAtBegin(30)
    ll.insertAtBegin(10)
    # Delete at nth Position
    ll.delete(20) # we can't delete at the 1st positon of the linked list 
    # Now traverse to get linked list 
    ll.traverse()
