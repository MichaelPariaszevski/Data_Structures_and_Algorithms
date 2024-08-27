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
           
    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################

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

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""