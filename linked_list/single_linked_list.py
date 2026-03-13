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