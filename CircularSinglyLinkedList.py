class Node:
    def __init__(self, value):
        self.value = value
        self.next_pointer = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current_node = self.head
        temp = self.head
        result = ""

        while current_node is not None:
            result += str(current_node.value)

            if current_node is not None:
                result += " -> "
            
            current_node = current_node.next_pointer

            if current_node == temp:
                break

        return f"{result}"

    def insert_at_first(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next_pointer = self.head
            self.head = node

        last_node = self.tail
        last_node.next_pointer = self.head

        self.show()

    def insert_at_last(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_pointer = node
            self.tail = node

        last_node = self.tail
        last_node.next_pointer = self.head

        self.show()
    
    def insert_at(self, value, index):
        node = Node(value)

        if index < 0 or index >= self.size(print_size = False):
            print("Index out of range")
        elif index == 0:
            self.insert_at_first(value)
        elif index == self.size(print_size = False) - 1:
            self.insert_at_last(value)
        else:
            current_node = self.head
            
            for _ in range(index - 1):
                current_node = current_node.next_pointer

            node.next_pointer = current_node.next_pointer
            current_node.next_pointer = node

            self.show()

    def delete_first_node(self):
        current_node = self.head.next_pointer
        self.head = current_node
        self.tail.next_pointer = current_node

        self.show()

    def delete_last_node(self):
        current_node = self.head

        for _ in range(self.size(print_size = False) - 2):
            current_node = current_node.next_pointer

        self.tail = current_node
        current_node.next_pointer = self.head

        self.show()
    
    def delete_node_at(self, index):
        if self.head is None:
            print("SLL is empty")
        elif index < 0 or index >= self.size(print_size = False):
            print("Index out of range")
        elif index == 0:
            self.delete_first_node()
        elif index == (self.size(print_size = False) - 1):
            self.delete_last_node()
        else:
            current_node = self.head

            for _ in range(index - 1):
                current_node = current_node.next_pointer

            current_node.next_pointer = current_node.next_pointer.next_pointer

            self.show()

    def delete_node(self, value):
        index = self.index_of(value, print_index = False)

        self.delete_node_at(index)

    def delete_all(self):
        self.head = None
        self.tail = None

        self.show()

    def reverse_csll(self):
        if self.head is None:
            print("SLL is empty")
        else:
            prev_node = None
            current_node = self.head
            
            while current_node is not None:
                next_node = current_node.next_pointer
                current_node.next_pointer = prev_node
                prev_node = current_node
                current_node = next_node
            
            self.head, self.tail = self.tail, self.head
                
            self.show()

    def node_at(self, index, print_node = True):
        current_node = self.head

        if self.head is None:
            print("CSLL is empty")
        elif index < 0 or index >= self.size(print_size = False):
            print("Index out of range")
        else:
            for _ in range(index):
                current_node = current_node.next_pointer

            if print_node:
                print(f"{current_node.value} found at index {index}")
            else:
                return current_node.value
            
    def index_of(self, value, print_index = True):
        current_node = self.head
        index = 0
        found = False

        while current_node is not None:
            index += 1

            if print_index:
                if current_node.value == value:
                    print(f"{value} found at index {index-1}")
                    
                    found = True
                    break
                else:
                    current_node = current_node.next_pointer
            else:
                return index
        
        if not found and print_index:
            print(f"{value} not found in SLL")

    def change_at_index(self, value, index):
        if index < 0 or index >= self.size(print_size = False):
            print("Index out of range")
        else:
            current_node = self.head

            for _ in range(index):
                current_node = current_node.next_pointer

            current_node.value = value

            self.show()

    def change_with_node(self, original_value, new_value):
        current_node = self.head
        found = True

        while current_node is not None:
            if current_node.value == original_value:
                current_node.value = new_value
                found = False
                
                self.show() 
                
                break
            else:
                current_node = current_node.next_pointer

        if found:
            print(f"{original_value} is not present in SLL")

    def show(self):
        if self.head is None:
            print("None")
        else:
            current_node = self.head
            temp = self.head
            result = ""

            while current_node is not None:
                result += str(current_node.value)

                if current_node is not None:
                    result += " -> "
                
                current_node = current_node.next_pointer

                if current_node == temp:
                    break

            print(f"{result}")

    def size(self, print_size=True):
        current_node = self.head
        temp = self.head
        self.length = 0

        while current_node is not None:
            current_node = current_node.next_pointer
            self.length += 1

            if current_node == temp:
                break

        if print_size:
            print(f"CSLL size = {self.length} \n")
        else:
            return self.length
      
csll = CircularSinglyLinkedList()

csll.insert_at_last(10)
csll.insert_at_last(20)
csll.insert_at_last(30)

csll.insert_at_first(-10)
csll.insert_at_first(-20)
csll.insert_at_first(-30)

csll.insert_at(0, 3)

csll.node_at(4)

csll.index_of(20)

csll.change_at_index(value = 5, index = 4)

csll.change_with_node(original_value = -10, new_value = -5)

csll.delete_first_node()

csll.delete_last_node()

csll.delete_node_at(3)

csll.delete_node(-5)

# csll.delete_all()

csll.reverse_csll()
