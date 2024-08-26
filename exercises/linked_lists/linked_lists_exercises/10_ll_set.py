class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


    def prepend(self, value): 
        new_node = Node(value) 
        if self.length == 0: 
            self.head = new_node 
            self.tail = new_node
            self.length += 1 
        else: 
            new_node.next = self.head 
            self.head = new_node
            self.length += 1 
        return True
    
    def pop_first(self): 
        if self.length == 0: 
            return None 
        temp = self.head
        if self.length == 1: 
            self.head = None 
            self.tail = None
            self.length -= 1
            return temp
        self.head = temp.next 
        temp.next = None 
        self.length -=1
        return temp
             
    def get(self, index): 
        if index < 0 or index >= self.length: 
            return None 
        temp = self.head
        for _ in range(index): 
            temp = temp.next 
        return temp
    
    def set_value(self, index, value): 
        if self.length == 0: 
            return False
        if index < 0 or index > self.length: 
            return False 
        elif index == 0: 
            self.head.value = value
            return True 
        elif index == self.length: 
            self.tail.value = value
            return True 
        else: 
            temp = self.get(index)
            temp.value = value
            return True  
        
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)

print('\nLL after set_value():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""