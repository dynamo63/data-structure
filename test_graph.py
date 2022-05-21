from pytest import fixture
from Graph import depth_first_traversal, breadth_first_traversal

@fixture
def graph_data() -> dict:
    data = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
    }
    return data

def test_dft(graph_data: dict):
    result = depth_first_traversal(graph_data, source='a')
    assert result in ['acebdf', 'abdfce']

def test_bft(graph_data: dict):
    result = breadth_first_traversal(graph_data, source='a')
    assert result in ['abcdef']
