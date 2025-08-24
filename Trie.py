from TrieNode import TrieNode

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()              # Root of the Trie (empty node, no character stored here)

    # Insert a word into the Trie
    def insert(self, word) -> None:
        curr = self.root

        # Traverse each character in the word
        for letter in word:
            index = curr.getIndex(letter)  # Convert letter → index (0–25)

            # If the child for this character does not exist, create it
            if curr.children[index] is None:
                curr.children[index] = TrieNode()

            # Move down to the child node
            curr = curr.children[index]

        # Mark the last node as the end of a valid word
        curr.isEndOfWord = True
