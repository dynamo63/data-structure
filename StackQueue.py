# Stack and Queue algo
from LinkedList import DoublyLinkedList

class Stack:
    """
        Implementation of Stack data structure with list
    """

    def __init__(self) -> None:
        self.stack_list = []
        self._stack_size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def size(self)-> int:
        return self._stack_size

    @size.setter
    def size(self, value):
        self._stack_size = value

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def push(self, value):
        self.size += 1
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        self.size -= 1
        return self.stack_list.pop()

class Queue:
    def __init__(self) -> None:
        self.items = DoublyLinkedList()

    def is_empty(self) -> bool:
        return self.items.is_empty()

    def front(self):
        return None if self.items.is_empty() else self.items.get_head()

    def rear(self):
        return None if self.items.is_empty() else self.items.tail_node()
    
    def size(self):
        return self.items.length

    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()
