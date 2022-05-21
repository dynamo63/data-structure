from pytest import fixture
from Heap import MinHeap, convert_max_heap
from random import sample

@fixture
def random_array() -> list:
    array = sample(range(0, 200), 8)
    return array

@fixture
def random_min_heap(random_array) -> MinHeap:
    capacity = 10
    min_heap = MinHeap(capacity)
    for n in random_array:
        min_heap.insert(n)
    return min_heap

def test_min_heap(random_min_heap: MinHeap, random_array: list):
    assert min(random_array) == random_min_heap.get_min()

def test_convert_max_heap(random_min_heap: MinHeap):
    heap = random_min_heap.get_list()
    print(heap)
    max_heap = convert_max_heap(heap)
    print('Max', max_heap[0])
    # assert max(heap) == max_heap[0]
