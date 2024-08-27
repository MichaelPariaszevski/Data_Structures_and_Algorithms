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
    
def find_kth_from_end(ll, k): 
    if ll.head == None: 
        return None 
    temp_fast = ll.head 
    temp_slow = ll.head
    for _ in range(k): 
        if temp_fast == None: 
            return None
        temp_fast = temp_fast.next 
    # loop_counter = 0
    while temp_fast is not None: 
        temp_fast = temp_fast.next 
        temp_slow = temp_slow.next 
        # loop_counter += 1
        # if loop_counter < k and temp_fast == None: 
        #     return None
        # elif loop_counter >= k and temp_fast == None: 
        #     return temp_slow
    return temp_slow
            
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2 # k < length of linked list
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

my_linked_list_2 = LinkedList(1) 
my_linked_list_2.head = None 
my_linked_list_2.tail = None

k = 1 # empty linked list 
result_2 = find_kth_from_end(my_linked_list_2, k) 

print(result_2)

my_linked_list_3 = LinkedList(1) 
my_linked_list_3.append(3)
my_linked_list_3.append(5)
my_linked_list_3.append(7)

k = 4 # k == length of linked list
result_3 = find_kth_from_end(my_linked_list_3, k)

print(result_3.value)

my_linked_list_4 = LinkedList(1) 
my_linked_list_4.append(2)
my_linked_list_4.append(4)
my_linked_list_4.append(6)

k = 5 # k > length of linked list
result_4 = find_kth_from_end(my_linked_list_4, k)

print(result_4)

"""
    EXPECTED OUTPUT:
    ----------------
    4
    None
    1
    None
"""

  


