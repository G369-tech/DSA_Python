class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning of the list
    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    # Insertion at the end of the list
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node

    # Insertion at a specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_beginning(data)
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

    # Deletion at the beginning of the list
    def delete_beginning(self):
        if not self.head:
            return
        if self.head == self.head.next:
            self.head = None
            return
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head = self.head.next

    # Deletion at the end of the list
    def delete_end(self):
        if not self.head:
            return
        if self.head == self.head.next:
            self.head = None
            return
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    # Deletion at a specific position
    def delete_at_position(self, position):
        if not self.head:
            return
        if position == 0:
            self.delete_beginning()
            return
        current = self.head
        for _ in range(position):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev

    # Display the linked list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    # Search for an element in the list
    def search(self, target):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.data == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    # Sort the linked list
    def sort(self):
        if not self.head:
            return
        current = self.head
        sorted_list = []
        while True:
            sorted_list.append(current.data)
            current = current.next
            if current == self.head:
                break
        sorted_list.sort()
        new_list = CircularDoublyLinkedList()
        for item in sorted_list:
            new_list.insert_end(item)
        self.head = new_list.head

# Example usage
cdll = CircularDoublyLinkedList()
cdll.insert_beginning(5)
cdll.insert_end(10)
cdll.insert_at_position(7, 1)
cdll.display()  # Output: 5 7 10
cdll.sort()
cdll.display()  # Output: 5 7 10
print(cdll.search(7))  # Output: True
cdll.delete_beginning()
cdll.delete_end()
cdll.display()  # Output: 7
