class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Insertion at a specific position
    def insert_at_position(self, data, position):
        if position <= 0:
            print("Invalid position")
            return
        if position == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 2):
            temp = temp.next
            if temp == self.head:
                print("Invalid position")
                return
        new_node.next = temp.next
        temp.next = new_node

    # Deletion from the beginning
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    # Deletion from the end
    def delete_from_end(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

    # Deletion from a specific position
    def delete_from_position(self, position):
        if position <= 0 or not self.head:
            print("Invalid position")
            return
        if position == 1:
            self.delete_from_beginning()
            return
        temp = self.head
        prev = None
        for _ in range(position - 1):
            prev = temp
            temp = temp.next
            if temp == self.head:
                print("Invalid position")
                return
        prev.next = temp.next

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    # Search for an element
    def search(self, target):
        if not self.head:
            print("List is empty")
            return False
        temp = self.head
        while True:
            if temp.data == target:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    # Sort the list
    def sort(self):
        if not self.head:
            print("List is empty")
            return
        sorted_list = []
        temp = self.head
        while True:
            sorted_list.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        sorted_list.sort()
        self.head = None
        for item in sorted_list:
            self.insert_at_end(item)

# Example usage
circular_list = CircularSinglyLinkedList()
circular_list.insert_at_end(10)
circular_list.insert_at_end(30)
circular_list.insert_at_beginning(5)
circular_list.insert_at_position(20, 2)
circular_list.display()

circular_list.delete_from_position(3)
circular_list.display()

print(circular_list.search(30))
print(circular_list.search(15))

circular_list.sort()
circular_list.display()
