class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count +=1
            node = node.next
        return count
    
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index out of range")
        node = self.head
        for i in range(index):
            node = node.next
        return node.data
    
    def __setitem__(self, index, value):
        if index >= len(self):
            raise IndexError("Index out of range")
        node = self.head
        for i in range(index):
            node = node.next
        node.data = value

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
                node.next = new_node
    
    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for i in range(index -1):
                node = node.next
                if node is None:
                    raise IndexError("Index out of range")
                
            new_node.next = node.next
            node.next = new_node

    def remove(self, value):  
        if self.head is None:
            raise ValueError("Value not found")
        elif self.head.data == value:
            self.head = self.head.next
        else:
            node = self.head
            while node.next and node.next.data != value:
                node = node.next
            if node.next is None:
                raise ValueError("Value not found")
            else:
                node.next = node.next.next

    def pop(self, index=-1):
        if self.head is None:
            raise IndexError("Index out of range")
        elif index == 0:
            value = self.head.data
            self.head = self.head.next
        else:
            node = self.head
            for i in range(index - 1):
                node = node.next
                if node is None:
                    raise IndexError("Index out of range")
                if index == -1:
                    index = len(self) - 1
                value = node.next.data
                node.next = node.next.next
            return value

    def index(self, value):
        index = 0
        node = self.head
        while node and node.data != value:
            node = node.next
            index += 1
        if node is None:
            raise ValueError("Value not found")
        else:
            return index

    def clear(self):
        self.head = None
            