from collections import defaultdict
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
# Represents a single node in the Trie


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = defaultdict(TrieNode)
        self.is_word = False
        self.word_list = []

    def suffixes(self):
        self.gather_words(self, '')
        return self.word_list

    def gather_words(self, node, word):
        if node.is_word:
            self.word_list.append(word)

        for key, t_node in node.children.items():
            self.gather_words(t_node, word + key)


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')
