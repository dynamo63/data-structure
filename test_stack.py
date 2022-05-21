import pytest
from StackQueue import Stack

@pytest.fixture
def mystack() -> Stack:
    stack = Stack()
    for i in range(8):
        stack.push(i)
    return stack

def test_is_empty():
    stack = Stack()
    assert stack.is_empty()

def test_push_element(mystack: Stack):
    current_size = mystack.size
    mystack.push(80)
    assert mystack.size == (current_size + 1)
    assert mystack.peek() == 80

def test_pop_element(mystack: Stack):
    current_size = mystack.size
    mystack.pop()
    assert mystack.size == (current_size - 1)
