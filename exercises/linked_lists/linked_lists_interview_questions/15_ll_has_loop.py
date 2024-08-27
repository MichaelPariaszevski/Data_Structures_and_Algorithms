class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self): 
        if self.head == None: 
            return None 
        temp_fast = self.head 
        temp_slow = self.head 
        while temp_fast.next is not None: 
            if temp_fast.next.next == None: 
                temp_slow.value += 1
                return temp_slow
            else: 
                temp_slow = temp_slow.next
                temp_fast = temp_fast.next.next
        if temp_slow.value % 2 != 0: 
            return temp_slow
        else: 
            temp_slow.value += 1
            return temp_slow
            
            
    # WRITE HAS_LOOP METHOD HERE #
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################
    
    def has_loop(self): 
        if self.head == None: 
            return False 
        temp_fast = self.head 
        temp_slow = self.head 
        while temp_fast.next is not None: 
            if temp_fast.next.next is None: 
                return False
            temp_fast = temp_fast.next.next 
            temp_slow = temp_slow.next 
            if temp_fast == temp_slow: 
                return True 
            else: 
                continue
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    """
            
  


