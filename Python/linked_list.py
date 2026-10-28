class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Display the list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Search for a value
    def search(self, key):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # Delete the first occurrence of a value
    def delete(self, key):
        if self.head is None:
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    # Reverse the list
    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


# Main program
ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_beginning(5)

print("Original list:")
ll.display()

print("Search 20:", ll.search(20))

ll.delete(20)
print("After deleting 20:")
ll.display()

ll.reverse()
print("After reversing:")
ll.display()
