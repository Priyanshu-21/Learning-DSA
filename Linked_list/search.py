# Search for element in linkedlist
'''
Time Complexity: - O(n)
Space Complexity: - O(n)
Insert element at beginning of linked list 
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
    
    def search(self, k):
        current = self.head
        while (not(current == None) and not(current.data == k)):
            current = current.next

        return current

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegin(10)
    ll.insertAtBegin(20)
    ll.insertAtBegin(5)
    ll.insertAtBegin(7)
    ll.insertAtBegin(8)
    # Include the Search Logic Here
    result = ll.search(12)
    print("Data found at location "+ str(result))