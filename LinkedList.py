# Here we create a common data structure named Linked List.

class Node:
    """
        A node is a element of linked list that contains data
    """
    def __init__(self, data) -> None:
        self.data = data # Save data(str, int, ...)
        self.next_element = None # save pointer(next node)
        self.previous_element = None #save previous element

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head_node = None # index the first node

    def is_empty(self) -> bool:
        return self.head_node is None

    def get_head(self) -> Node:
        return self.head_node

    def search(self, value) -> Node:
        current_node = self.get_head()
        while current_node.next_element:
            if current_node.data == value:
                return current_node
            current_node = current_node.next_element
        return None

    def delete(self, value) -> bool:
        if self.is_empty():
            return False
        current_node = self.get_head()
        previous_node = self.get_head()
        while current_node:
            if current_node.data is value:
                previous_node.next_element = current_node.next_element
                del current_node
                return True
            previous_node = current_node
            current_node = current_node.next_element
        return False

    def length(self) -> int:
        if self.is_empty():
            return 0
        current_node = self.get_head()
        i = 0
        while current_node:
            i += 1
            current_node = current_node.next_element
        return i

    def insert_at_head(self, data) -> Node:
        """
            This method allow to insert a data in the first 
            node in our Linked List.
        """
        # Create a node containing the specified data
        new_node = Node(data)
        # index the head current node
        new_node.next_element = self.head_node
        # index the new node
        self.head_node = new_node
        return self.head_node
    
    def insert_at_tail(self, data) -> Node:
        """
            This method allow to insert a data in the last 
            node in Linked List.
            Sample: 0 -> 1 -> None ,we insert at tail 2
            ----------
            Result: 0 -> 1 -> 2 -> None
        """
        temp_node = Node(data)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node
        current_node = self.get_head()
        while current_node.next_element is not None:
            current_node = current_node.next_element
        current_node.next_element = temp_node
        return temp_node

    def insert(self, data, k: int) -> Node:
        """
            Insert a data to the k'th position in LinkedList
        """
        new_node = Node(data)
        if self.is_empty():
            if k != 0:
                raise IndexError("This list is empty, try to use insert_at_head")
            else:
                self.head_node = new_node
                return self.head_node
        i = 0
        current_node = self.head_node
        while current_node.next_element is not None:
            if i == k:
                temp_node = current_node.next_element
                current_node.next_element = new_node
                new_node.next_element = temp_node
                break
            else:
                i +=1
                current_node = current_node.next_element
        if i < k:
            raise IndexError("Index too great")
        return current_node.next_element

    def print_list(self) -> None:
        """
            Print the linked list: a -> b -> ... -> None
        """
        if self.is_empty():
            print("Empty List")
            return None
        current_node = self.get_head()
        print('Linked List')
        print('---' * 20)
        while current_node.next_element is not None:
            print(f"{current_node.data}", end=" -> ")
            current_node = current_node.next_element
        print()
        print('---' * 20)
        return None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if (self.head != None):
            return self.head.data
        else:
            return False

    def is_empty(self):
        if(self.head is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, element):
        temp_node = Node(element)
        if(self.is_empty()):
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length+=1
        return temp_node.data


    def remove_head(self):
        if(self.is_empty()):
            return False
        nodeToRemove = self.head;
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = nodeToRemove.next_element
            self.head.previous_element = None
            nodeToRemove.next_element = None
        self.length-=1
        return nodeToRemove.data
  

    def tail_node(self):
        if (self.head != None):
            return self.tail.data
        else:
            return False
   
    def __str__(self):
        val=""
        if(self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while (temp.next_element):
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val


