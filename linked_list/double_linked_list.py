# Double linked list operations (inser, delete, search and traversal)

class DoubleNode():
    def __init__(self, data):
        self.data = data
        self.next = None    # Next reference to node
        self.prev = None    # Previous refrence to node

class DoubleLinkedList():
    def __init__(self):
        self.head = None
    
    # Insert at beginging 
    def insert_at_beg(self, data):
        
        new_node = DoubleNode(data) # creating new node with data inside. 
        if (self.head == None):
            self.head = new_node
            new_node.prev = self.head 
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = self.head 
        
        return self.head
    
    # Insert at end 
    def insert_at_end(self, data):

        new_node = DoubleNode(data)
        # if head is null, point it to new_node  
        if (self.head == None):
            self.head = new_node 
            new_node.prev = self.head 
        
        else:
            # Traverse to the end of node 
            curr = self.head 
            while curr.next != None:
                curr = curr.next
            curr.next = new_node 
            new_node.prev = curr 

        return self.head 

    # Insert values at the middle 
    def insert_at_middle(self, data):

        new_node = DoubleNode(data)
        # head node is null 
        if (self.head == None):
            self.head = new_node 
            new_node.prev = self.head
        else: 
            # Traverse to calculate num of nodes 
            curr = self.head 
            n = 0
            while curr != None: 
                n += 1
                curr = curr.next

            # Calculate middle node and insert at this position, 
            # move nodes to shift right
            n = n // 2
            next_node = self.head 
            while (n - 1) != 0:
                prev = next_node
                next_node = next_node.next
                n -= 1
            # Adding node at this position and moving others to shift right 
            prev.next = new_node
            new_node.next = next_node
            new_node.prev = prev 
            next_node.prev = new_node

        return self.head 

    # Delete at begining
    def delete_at_begin(self):
        # Only one node is present to be deleted 
        if (self.head.next == None):
            self.head = None  
        else: 
            current = self.head 
            self.head = current.next 
            current.prev = None
            current.next.prev = None
        
        return self.head 

    # Delete at end 
    def delete_at_end(self):
        # Only one node is there in ll 
        if (self.head.next == None):
            self.head = None
        else: 

            # Traverse through end of ll 
            curr = self.head 
            while (curr.next != None):
                previous = curr
                curr = curr.next 
            
            previous.next = None
            curr.prev = None
        
        return self.head 
    
    # Delete at middle 
    def delete_at_middle(self):
        # Only one node is there in ll 
        if (self.head.next == None):
            self.head = None
        else: 

            # Traverse to get number of node in ll 
            curr = self.head
            n = 0
            while (curr != None):
                n += 1
                curr = curr.next
            
            # Get middle of node (for odd and even values)
            n = n // 2 - 1 if (n % 2 == 0) else n // 2
            curr = self.head    # Re-assigned current to start from head 
            while n != 0:
                previous = curr
                curr = curr.next
                n -= 1
            # We have to remove current node 
            previous.next = curr.next
            curr.next.prev = previous
            curr.prev = None
            curr.next = None
        
        return self.head 

    def find_element(self, key):
        
        curr = self.head 
        n = 0
        while (curr != None):
            if (curr.data == key):
                return n + 1
            curr = curr.next 
            n += 1
        
        return -1

    # Traversal and print values 
    def print_values(self):
        # Traversing each node 
        temp = self.head 
        while temp != None:
            print(temp.data, " ")
            temp = temp.next 
        
if __name__ == "__main__":
    dll = DoubleLinkedList()
    insert = dll.insert_at_beg(10)
    insert = dll.insert_at_beg(20)
    insert = dll.insert_at_beg(30)
    insert = dll.insert_at_beg(40)
    dll.print_values()
    print('Double-linked list: Insert at end')
    insert = dll.insert_at_end(55)
    dll.print_values()
    print('Double-linked list: Insert at middle')
    insert = dll.insert_at_middle(21)
    dll.print_values()
    print('Double-linked list: Delete at Begin')
    delete = dll.delete_at_begin()
    dll.print_values()
    print('Double-linked list: Delete at End')
    delete = dll.delete_at_end()
    dll.print_values()
    print('Double-linked list: Delete at Middle')
    delete = dll.delete_at_middle()
    dll.print_values()
    find = dll.find_element(31)
    print(f'Element found at location {find} ')
