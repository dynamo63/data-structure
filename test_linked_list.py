import pytest
from LinkedList import SinglyLinkedList

@pytest.fixture
def singlyList():
    linked_list = SinglyLinkedList()
    for i in range(1, 10, -1):
        linked_list.insert_at_head(i)
    return linked_list

def test_is_empty():
    linkedList = SinglyLinkedList()
    assert linkedList.is_empty()

def test_insert_at_head(singlyList: SinglyLinkedList):
    singlyList.insert_at_head("hello")
    head_node = singlyList.get_head()
    assert head_node.data == "hello"