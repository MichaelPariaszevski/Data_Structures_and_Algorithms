class Node(): 
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None
        
                
class LinkedList(): 
    def __init__(self, value) -> None:
        new_node = Node(value) 
        self.head = new_node 
        self.tail = new_node 
        self.length = 1
        
        
    def print_list(self): 
        temp = self.head 
        while temp is not None: # temp, not temp.next here
            print(temp.value) 
            temp = temp.next
            
    def append(self, value): 
        new_node = Node(value) 
        
        if self.head is None: 
            self.head = new_node 
            self.tail = new_node
        else: 
            self.tail.next = new_node 
            self.tail = new_node
        
        self.length += 1