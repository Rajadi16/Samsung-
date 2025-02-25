class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)  # Fixed the typo (was new1_node)
        if not self.head:
            self.head = new_node  # Fixed incorrect variable reference
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, data, pos):
        """Insert a node at a specific position"""
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 1):
            if not temp:
                print("Position out of bounds!")
                return
            temp = temp.next
        if not temp:
            print("Position out of bounds!")
            return
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_position(self, pos):
        """Delete a node from a specific position"""
        if not self.head:
            print("List is empty!")
            return
        temp = self.head

        if pos == 0:
            self.head = temp.next
            temp = None
            return

        prev = None
        for _ in range(pos):
            prev = temp
            temp = temp.next
            if not temp:
                print("Position out of bounds!")
                return

        prev.next = temp.next
        temp = None

    def display(self):
        """Display the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Linked List reversed!")
        

def menu():
    ll = LinkedList()

    while True:
        print("\n----- Linked List Operations -----")
        print("1. Append")
        print("2. Insert at Position")
        print("3. Delete from Position")
        print("4. Display")
        print("5. Reverse")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                data = int(input("Enter value to append: "))
                ll.append(data)
            case 2:
                data = int(input("Enter value to insert: "))
                pos = int(input("Enter position: "))
                ll.insert_at_position(data, pos)
            case 3:
                pos = int(input("Enter position to delete: "))
                ll.delete_at_position(pos)
            case 4:
                ll.display()
            case 5:
                ll.reverse()
                ll.display()
                ll.reverse()
               
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid choice! Try again.")

menu()
