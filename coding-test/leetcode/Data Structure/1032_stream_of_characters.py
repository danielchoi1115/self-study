# https://leetcode.com/problems/stream-of-characters/
# 1032. Stream of Characters

from collections import deque
from typing import List

class StreamChecker:
    class cTrie:
        def __init__(self, value):
            self.value = value
            self.isWord = False
            self.children = {}
        def __repr__(self) -> str:
            return str(f"cTrie('{self.value}', isWord={self.isWord})")
    
    def __init__(self, words: List[str]):
        self.pointers = {}
        self.stream = ''
        for word in words:
            current_node = None
            for i in range(2, len(word)+2):
                c = word[:-i:-1]
                if current_node is None and c in self.pointers:
                    current_node = self.pointers[c]
                    continue
                elif current_node is not None and c in current_node.children:
                    current_node = current_node.children[c]
                    continue 
                
                node = self.cTrie(c)
                if current_node is None:
                    self.pointers[c] = node
                elif current_node is not None:
                    current_node.children[c] = node
                current_node = node
            current_node.isWord = True

    def query(self, letter: str) -> bool:
        current_node = None
        self.stream = letter + self.stream
        for i in range(1, len(self.stream)+1):
            c = self.stream[:i]
            if current_node is None:
                node = self.pointers.get(c)
            else:
                node = current_node.children.get(c)
            current_node = node
            if node is None:
                return False
            elif node.isWord:
                return True
                
        return False


class StreamChecker2:
    def __init__(self, words: List[str]):
        self.stream = deque()
        self.trie = {}
        self._makeTrie(words)
    
    def __repr__(self) -> str:
        return str(f"StreamChecker({''.join(self.stream)})")
        
    def _makeTrie(self, words):
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['end'] = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if node.get('end'):
                return True
            if c not in node:
                return False
            node = node[c]
        return 'end' in node



streamChecker = StreamChecker2(["ab","ba","aaab","abab","baa"])

q = [["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]

for i in q:
    print(streamChecker.query(i[0]))