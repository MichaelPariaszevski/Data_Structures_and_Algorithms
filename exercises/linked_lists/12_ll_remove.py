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
        
    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0 and index == 0: 
            self.head = new_node 
            self.tail = new_node
            self.length += 1
            return True
        if index < 0 or index > self.length: 
            return False 
        if index == 0: 
            self.prepend(value)
            self.length += 1
            return True 
        if index == self.length: 
            self.append(value) 
            self.length += 1
            return True
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node 
        self.length += 1
        return True
    
    def remove(self, index): 
        if index < 0 or index >= self.length: 
            return None 
        if index == 0: 
            temp = self.pop_first() 
            return temp 
        if index == self.length - 1: 
            temp = self.pop() 
            return temp
        prev = self.get(index - 1) 
        temp = prev.next 
        prev.next = temp.next 
        temp.next = None 
        self.length -= 1 
        return temp
    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('LL before remove():')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() in middle:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(0).value)
print('LL after remove() of first node:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() of last node:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    LL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    LL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    LL after remove() of last node:
    2
    4

"""