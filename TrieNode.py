class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26         # Number of possible children (number of letters in alphabet)
        self.isEndOfWord = False            # Bool that represents if the letter is an end of word

    # Auxiliary function that returns the index of a letter at the array of children
    def getIndex(self, letter) -> int:
        return ord(letter) - ord('A')
