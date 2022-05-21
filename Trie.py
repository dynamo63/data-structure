from typing import List

class TrieNode:
    def __init__(self, char="") -> None:
        self.children = [None] * 26 #max size: alphabet size
        self.char = char
        self.end_of_words = False

def find_words(root):
    def get_all(node,cum, prefix):
        if node is None: 
            return 
        word = node.char 
        prefix += word
        if node.end_of_words:
            cum.append(prefix)
        for n in node.children:
            if n is not None:
                word += get_all(n, cum, prefix)
        return word
    cum = []
    p = ""
    get_all(root,cum, p) # override cum and add all word in root
    return cum

def count_all_children(node: TrieNode, cum: list) -> int:
    # educative solution
    # def total_words(root):
    #     result = 0

    #     # Leaf denotes end of a word
    #     if root.is_end_word:
    #         result += 1

    #     for letter in root.children:
    #         if letter is not None:
    #             result += total_words(letter)
    #     return result
    all_node: List[TrieNode] = filter(lambda n: n is not None, node.children)
    if all_node is []:
        return 
    for n in all_node:
        cum.append(n.end_of_words)
        count_all_children(n,cum)
    return cum

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def get_index(self, c):
        return ord(c) - ord('a')

    def insert(self, key: str) -> bool:
        if key is None:
            return False
        current = self.root
        key = key.lower()
        for l in key:
            try:
                i = self.get_index(l)
                if current.children[i] is None:
                    current.children[i] = TrieNode(l)
                current = current.children[i]
            except IndexError:
                return False
        current.end_of_words = True

    def search(self, key: str) -> bool:
        if key is None:
            return False
        key = key.lower()
        current = self.root
        for l in key:
            i = self.get_index(l)
            if current.children[i] is None:
                return False
            current = current.children[i]
        if current is not None and current.end_of_words:
            return True
        return False

    def autocomplete(self, key:str) -> list:
        if key is None:
            return []
        key = key.lower()
        current = self.root
        for l in key:
            i = self.get_index(l)
            current = current.children[i]
        if current is not None:
            prefix = key
            res = []
            result = self.get_all_children(current,res, current)
            suffix = ""
            suggests = []
            for l in result:
                if l == '/':
                    suggests.append(prefix+suffix)
                    suffix = ""
                    continue
                elif l == '#':
                    suggests.append(prefix+suffix)
                    continue
                suffix += l
            return suggests
    
    def get_all_children(self, node: TrieNode, cum: List[str], root: TrieNode) -> List[str]:
        all_node :List[TrieNode]= filter(lambda n: n is not None, node.children)
        if all_node is []:
            return None
        for n in all_node:
            cum.append(n.char)
            if n.end_of_words and any(n.children):
                cum.append('#')
            self.get_all_children(n, cum, root=root)
        if node in root.children:
            cum.append('/')
        return cum
