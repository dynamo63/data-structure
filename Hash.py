# Here we learn about Hash Table, The ideal data structure to insertion,deletion and search
# In python, Hash table can be implemented with set or dict

from typing import Any, List, Optional


def modular_arithmetic(code: int, slot: int) -> int:
    return code % slot

class HashEntry:
    def __init__(self, key: int, data:Any) -> None:
        self.key = key
        self.value = data
        self.next = None

    def __str__(self) -> str:
        return f"{self.key} ==> {self.value}"

class HashTable:
    def __init__(self) -> None:
        self.slots = 10 # Fixe size of HashTable
        self.size = 0 # current entries in the table
        self.bucket: List[Optional[HashEntry]] = [None] * self.slots
        self.threshold: float = 0.6

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def get_index(self, key: Any) -> int:
        hash_code = hash(key)
        index = modular_arithmetic(hash_code, self.slots)
        return index

    def resize(self) -> None:
        """
            Method to use to resize the HashTable
        """
        # Define new size
        new_slots: int = self.slots * 2
        new_bucket: List[Optional[HashEntry]] = [None] * new_slots

        for item in self.bucket:
            head = item
            while head is not None:
                new_index = modular_arithmetic(head.key, new_slots)
                if new_bucket[new_index] is None:
                    new_bucket = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key == head.key:
                            node.value = head.value
                            node = None
                        elif node.next is None:
                            node.next = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.next
                head = head.next
            self.bucket = new_bucket
            self.slots = new_slots
    
    def insert(self, key: int, value: Any) -> int:
        """
            Insert a value in the HashTable
        """
        b_index = self.get_index(key)
        if self.bucket[b_index] is None:
            self.bucket[b_index] = HashEntry(key, value)
            self.size += 1
        else:
            node = self.bucket[b_index]
            while node is not None:
                if node.key == key:
                    node.value = value
                    break
                elif node.next is None:
                    node.next = HashEntry(key, value)
                    self.size += 1
                    break
                node = node.next
        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()
        return key

    def search(self, key:int) -> Any:
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def delete(self, key) -> bool:
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        if head is None:
            return False
        if head.key == key:
            head = head.next
            self.size -= 1
            return True
        prev_node = None
        while head is not None:
            if head.key == key:
                prev_node.next = head.next
                self.size -= 1
                return True
            prev_node = head
            head = head.next
        return False
