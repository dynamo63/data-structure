# Heap data structure
from typing import Optional
import math

class MinHeap:
    def __init__(self, capacity: int) -> None:
        """
            capacity is the max space into our heap
        """
        self.heap = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def __get_parent_index(self, index: int) -> int:
        return (index - 1)//2

    def __get_left_index(self, index: int) -> Optional[int]:
        if index > self.size:
            return None
        return 2 * index + 1

    def __get_right_index(self, index: int) -> Optional[int]:
        if index > self.size:
            return None
        return 2 * index + 2

    def has_parent(self, index) -> bool:
        return self.__get_parent_index(index) >= 0

    def get_min(self) -> int:
        return self.heap[0]

    def get_list(self) -> list:
        return list(filter(lambda x: x is not None, self.heap))

    def has_left_child(self, index:int) -> bool:
        return self.__get_left_index(index) != None

    def has_right_child(self, index:int) -> bool:
        return self.__get_right_index(index) != None
    
    def get_parent(self, index:int) -> int:
        return self.heap[self.__get_parent_index(index)]
    
    def get_left(self, index: int) -> int:
        return self.heap[self.__get_left_index(index)]

    def get_right_child(self, index: int) -> int:
        return self.heap[self.__get_right_index(index)]

    def is_full(self) -> bool:
        return self.size == self.capacity
    
    def swap(self, index1: int, index2: int) -> None:
        try:
            temp = self.heap[index1]
            self.heap[index1] = self.heap[index2]
            self.heap[index2] = temp
        except IndexError:
            raise('Just input the good index')
        return
    
    def insert(self, value: int):
        if self.is_full():
            raise("Heap is Full")
        self.heap[self.size] = value
        self.size += 1
        self.heapify_up(self.size - 1)

    # def __str__(self) -> str:
    #     return " ".join(self.heap)

    def heapify_up(self, index):
        """
            We check if the last value inserted is smaller than her parent,
            if it's the case: we swap value
        """
        if(self.has_parent(index) and self.get_parent(index) > self.heap[index]):
            self.swap(self.__get_parent_index(index), index)
            index = self.__get_parent_index(index)
            self.heapify_up(index)

def max_heapify_up(heap: list, index) -> None:
    """
        Convert a MinHeap to MaxHeap
    """
    largest = index
    left_index = (2 * index) + 1
    right_index = (2 * index) + 2
    if len(heap) > left_index and heap[left_index] > heap[largest]:
        largest = left_index
    if len(heap) > right_index and heap[right_index] > heap[largest]:
        print('2',heap[right_index], heap[largest])
        largest = right_index 
    print('-'*15)
    if largest != index:
        # Swap value
        print('swap')
        tmp = heap[largest]
        heap[largest] = heap[index]
        heap[index] = tmp
        max_heapify_up(heap, largest)
    
def convert_max_heap(heap: list) -> list:
    for i in range(len(heap)//2, -1, -1):
        max_heapify_up(heap, i)
    return heap
