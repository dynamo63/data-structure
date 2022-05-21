import pytest
from StackQueue import Queue

@pytest.fixture
def myqueue():
    queue = Queue()
    for i in range(1, 11):
        queue.enqueue(i)
    return queue

def test_empty_queue():
    myqueue = Queue()
    assert myqueue.is_empty()
    assert myqueue.front() is None
    assert myqueue.rear() is None
    assert myqueue.size() == 0

def test_enqueue_value(myqueue: Queue):
    current_size = myqueue.size()
    myqueue.enqueue(13)
    assert myqueue.size() == (current_size + 1)

def test_dequeue(myqueue: Queue):
    current_size = myqueue.size()
    myqueue.dequeue()
    assert myqueue.size() == (current_size - 1)
