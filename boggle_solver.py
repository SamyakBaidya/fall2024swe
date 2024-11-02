"""
Name: Sunishchit Ghimire
SID: @03087256
"""


class Boggle:
    def __init__(self, grid, dictionary):
        # Convert the grid to lowercase
        self.grid = [[letter.lower() for letter in row] for row in grid]
        # Convert the dictionary to lowercase
        self.dictionary = set(word.lower() for word in dictionary)
        self.solution = []

    def validate_grid(self):
        for row in self.grid:
            for cell in row:
                if cell == "q" or cell == "s":
                    # Raw "Q" or "S" is not allowed
                    return False
                elif cell != "qu" and cell != "st" and len(cell) > 1:
                    # Only "Qu" and "St" should be multi-letter tiles
                    return False
        return True

    def setGrid(self, grid):
        # Setter method to update the grid (convert to lowercase).
        self.grid = [[letter.lower() for letter in row] for row in grid]
        print(self.grid)

    def setDictionary(self, dictionary):
        # Setter method to update the dictionary (convert to lowercase).
        self.dictionary = set(word.lower() for word in dictionary)

    def getSolution(self):
        if not self.validate_grid():
            return []

        self.solution = []
        # Create a visited matrix to keep track of visited cells
        visited = [[False] * len(self.grid[0]) for _ in range(len(self.grid))]

        # Start DFS from each cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                self.dfs(row, col, "", visited)

        # Return the sorted list of found words
        return sorted(self.solution)

    def dfs(self, row, col, path, visited):
        # Check boundaries and if cell is already visited
        if (row < 0 or row >= len(self.grid) or
                col < 0 or col >= len(self.grid[0]) or
                visited[row][col]):
            return

        # Add the current cell's letter(s) to the path
        path += self.grid[row][col]

        # If path length is at least 3 and it is a valid word, add to solution
        if len(path) >= 3 and path in self.dictionary:
            if path not in self.solution:
                self.solution.append(path)

        # Check if the current path can be a prefix
        if not any(word.startswith(path) for word in self.dictionary):
            return

        # Mark the current cell as visited
        visited[row][col] = True

        # Explore all 8 possible directions from the current cell
        for r_offset, c_offset in [(-1, -1), (-1, 0), (-1, 1),
                                   (0, -1), (0, 1),
                                   (1, -1), (1, 0), (1, 1)]:
            new_row, new_col = row + r_offset, col + c_offset
            self.dfs(new_row, new_col, path, visited)

        # Unmark the current cell
        visited[row][col] = False


def main():
    # Define the grid and dictionary
    grid = [["A", "B", "Qu"], ["D", "Q", "F"], ["G", "H", "I"]]

    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]

    # Create a Boggle game instance
    mygame = Boggle(grid, dictionary)

    # Print the solution
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
