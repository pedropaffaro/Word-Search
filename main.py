"""
    Word Search Solver using Trie and Backtracking.

    Given a grid of letters and a dictionary of words:
    - Each word can be formed by starting at any cell
    - A fixed direction (horizontal, vertical, or diagonal) is chosen
    - The search continues in that direction until the word ends or fails

    @author: Pedro Paffaro
"""

from Trie import Trie

# All 8 possible directions (vertical, horizontal, diagonal)
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def word_search_algorithm(i, j, di, dj, node, path, grid, found):
    # Stop if outside grid boundaries
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    
    letter = grid[i][j]
    index = ord(letter) - ord('A')

    # Stop if no continuation in Trie
    if node.children[index] is None:
        return
    
    # Move to the child node in Trie
    node = node.children[index]
    path.append(letter)  # Add current letter to the word being formed

    # If this node marks the end of a word, add to results
    if node.isEndOfWord:
        found.add("".join(path))

    # Continue recursively in the same direction
    word_search_algorithm(i + di, j + dj, di, dj, node, path, grid, found)

    # Backtrack: remove last added letter before returning
    path.pop()

def find_words(grid, trie):
    found = set()  # Stores all unique words found

    # Iterate over each cell of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Try all 8 directions starting from this cell
            for di, dj in directions:
                word_search_algorithm(i, j, di, dj, trie.root, [], grid, found)

    return found

if __name__ == "__main__":
    trie = Trie()

    # Read grid dimensions
    entry = input()
    lines, columns = map(int, entry.split())

    # Read grid
    word_search = []
    for _ in range(lines):
        line = input().strip()
        word_search.append(list(line))

    # Insert dictionary words into Trie
    number_of_words_in_dictionary = int(input()) 
    for _ in range(number_of_words_in_dictionary):
        trie.insert(input().strip())

    # Run search
    found_words = find_words(word_search, trie)
    
    # Print results
    print(len(found_words))
    for word in sorted(found_words):
        print(word)
