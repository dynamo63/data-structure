from pytest import fixture
from Hash import HashTable

@fixture
def sample_one()-> HashTable:
    data = HashTable()
    data.insert(1, "Python")
    data.insert(2, "Javascript")
    data.insert(3, "HTML5")
    return data

def test_search(sample_one: HashTable):
    assert sample_one.search(1) == "Python"
    assert sample_one.search(3) == "HTML5"

def test_delete(sample_one: HashTable):
    assert sample_one.delete(1)
    assert not sample_one.delete(10)

