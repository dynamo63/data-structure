from typing import List
from pytest import fixture
from Trie import Trie, count_all_children, find_words

@fixture
def bag_of_words() -> List[str]:
    # TODO: Jason break autocompletion, take a look
    words = [
        "python","JavaScript", "HTML",
        "Docker", "Django", "Reactjs","Java","Jquery",
    ]
    return words

@fixture
def root(bag_of_words: List[str]) -> Trie:
    r = Trie()
    for word in bag_of_words:
        r.insert(word)
    return r

def test_search_in_trie(root: Trie):
    assert root.search("python")
    assert root.search("Django")
    assert root.search("jquery")
    assert root.search("java")
    assert root.search("javascript")

def test_autocomplete(root: Trie):
    suggests = root.autocomplete("D")
    assert "django" in suggests
    assert "bob" not in suggests
    # java - javascri - jquery
    suggests = root.autocomplete("j")
    assert "jquery" in suggests

def test_total_number_words(root: Trie, bag_of_words: List[str]):
    cum = []
    count_all_children(root.root, cum=cum)
    assert cum.count(True) == len(bag_of_words)

def test_find_words(root: Trie):
    words = find_words(root.root)
    print(words)
    