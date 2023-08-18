class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    return
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def delete_at_end(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            if current.prev:
                current.prev.next = None
            else:
                self.head = None

    def delete_at_position(self, position):
        if position <= 0:
            self.delete_at_beginning()
        else:
            current = self.head
            for _ in range(position):
                if current is None:
                    return
                current = current.next
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            position += 1
            current = current.next
        return -1

    def sort(self):
        if not self.head:
            return
        sorted_list = []
        current = self.head
        while current:
            sorted_list.append(current.data)
            current = current.next
        sorted_list.sort()
        self.head = None
        for item in sorted_list:
            self.insert_at_end(item)

# Example usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.insert_at_position(15, 2)
dll.display()

dll.delete_at_position(2)
dll.delete_at_end()
dll.delete_at_beginning()
dll.display()

print("Position of 20:", dll.search(20))

dll.insert_at_end(25)
dll.insert_at_beginning(2)
dll.insert_at_position(18, 2)
dll.display()

dll.sort()
dll.display()
