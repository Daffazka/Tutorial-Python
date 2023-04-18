class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
 
    def display(self):
        node_list = []
        current_node = self.head
        while current_node:
            node_list.append(current_node.data)
            current_node = current_node.next
        print(node_list)
 
    def selection_sort(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next:
            min_node = current_node
            iterator_node = current_node.next
            while iterator_node:
                if iterator_node.data < min_node.data:
                    min_node = iterator_node
                iterator_node = iterator_node.next
            if current_node != min_node:
                current_node.data, min_node.data = min_node.data, current_node.data
            current_node = current_node.next

# contoh penggunaan
my_list = LinkedList()
my_list.append(8)
my_list.append(7)
my_list.append(1)
my_list.append(4)
my_list.append(6)
my_list.append(2)
my_list.append(3)

print("Sebelum diurutkan:")
my_list.display()

my_list.selection_sort()

print("\nSetelah diurutkan:")
my_list.display()
