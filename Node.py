class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        if index < 0:
            raise ValueError("Index cannot be negative")

        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index < 0:
            raise ValueError("Index cannot be negative")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Index out of range")
            current = current.next
        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None

    def rotate(self, k):
        if self.head is None or k <= 0:
            return

        length = self.size()
        k %= length
        if k == 0:
            return

        prev = None
        current = self.head
        for _ in range(length - k):
            prev = current
            current = current.next
        prev.next = None

        new_head = current
        while current.next:
            current = current.next
        current.next = self.head
        self.head = new_head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other):
        if self.head is None:
            self.head = other.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other.head

    def interleave(self, other):
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            next_self = current_self.next
            next_other = current_other.next
            current_self.next = current_other
            current_other.next = next_self
            current_self = next_self
            current_other = next_other

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def find_index_of(self, data):
        index = 0
        current = self.head
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()  
linked_list.reverse()
linked_list.display()  

print("Size:", linked_list.size())  

print("Middle element:", linked_list.find_middle()) 
linked_list.insert_at_index(2, 10)
linked_list.display()  
linked_list.delete_at_index(1)
linked_list.display()  

print("Index of 10:", linked_list.find_index_of(10)) 

print("Is empty?", linked_list.is_empty())
