## Introduction to single linked list (insert, delete, search, traversal)

class Node:
    def __init__(self, data):
        self.data = data # Data node 
        self.next = None # Next node will have access to next node memory reference 


class SingleLinkedList():
    def __init__(self) -> None:
        super().__init__()
        self.head = None # Head node of ll is pointing to null value at initial 
    
    # Inserting values at the begining
    def insert_at_begin(self, data: int):
        
        new_node = Node(data)
        # Check if head == Null, then assign node value to head 
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head # type: ignore
            self.head = new_node

        return self.head

    # To insert values at the end 
    def insert_at_end(self, data: int):

        new_node = Node(data)
        # Check if head == Null, then assign node value to head 
        if self.head == None:
            self.head = new_node
        
        else:
            temp = self.head 
            while temp.next != None:
                temp = temp.next
            
            temp.next = new_node # type: ignore
        
        return self.head

    # To insert node at middle 
    def insert_at_middle(self, data: int):

        new_node = Node(data)
        # Check if head == null, then assign node value to head
        if self.head == None:
            self.head = new_node
        
        else:
            # Traverse through end of ll and calculate number of nodes 
            n = 0
            temp = self.head 
            while temp.next != None:
                n += 1
                temp = temp.next
            
            # Calculate middle node value
            n = n // 2
            new_temp = self.head 
            while n:
                new_temp = new_temp.next # type: ignore
                n -= 1
            new_node.next = new_temp.next # type: ignore
            new_temp.next = new_node # type: ignore
        
        return self.head

    # Delete at begining 
    def delete_at_begin(self):
        # Check if head.next is not null 
        if self.head.next == None:
            self.head = None # empty linked list 
        else: 
            next_node = self.head.next
            self.head.next = None
            self.head = next_node 
            
        return self.head

    # Delete at end 
    def delete_at_end(self):
        # Check if only 1 node is there or not 
        if self.head.next == None:
            self.head = None # delete that node and make head == Null 
        else: 
            # Traverse through end of node and delete it
            curr = self.head 
            while curr.next != None:
                prev = curr
                curr = curr.next
            
            # change end node next to point to null 
            prev.next = None
        
        return self.head

    # Delete at middle 
    def delete_at_middle(self):
        # Only one node is there in the list to delete
        if self.head.next == None:
            self.head = None
        else: 
            n = 0
            # Traverse through node (calculate n)
            curr = self.head
            while curr.next != None:
                n = n + 1
                curr = curr.next 
            
            # Calculate middle node. 
            n = n // 2
            curr = self.head 
            while n:
                prev = curr
                curr = curr.next 
                n = n - 1
            
            prev.next = curr.next 
            curr.next = None

            return self.head

    # To print values in linkedlist 
    def print_values(self):
        # Traverse through each value of data through temp node 
        temp = self.head 
        while temp != None:
            print(temp.data)
            temp = temp.next


# Main module 
if __name__ == "__main__":
    single_linked = SingleLinkedList()
    first_node = single_linked.insert_at_begin(10)
    first_node = single_linked.insert_at_begin(20)
    first_node = single_linked.insert_at_begin(30)
    last_node = single_linked.insert_at_end(40)
    last_node = single_linked.insert_at_end(45)
    last_node = single_linked.insert_at_end(70)
    middle_node = single_linked.insert_at_middle(99)
    middle_node = single_linked.insert_at_middle(100)
    middle_node = single_linked.insert_at_middle(101)
    middle_node = single_linked.insert_at_middle(102)
    single_linked.print_values()
    delete_node = single_linked.delete_at_begin()
    print("Linked List after deletion at beg:")
    single_linked.print_values()
    print("Linked List after deleting at last:")
    delete_node = single_linked.delete_at_end()
    single_linked.print_values()
    print("Linked List after deleting at middle:")
    delete_node = single_linked.delete_at_middle()
    single_linked.print_values()