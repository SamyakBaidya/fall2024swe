import sys
import unittest
from boggle_solver import Boggle


class TestSuiteAlgScalabilityCases(unittest.TestCase):
    # ADD 4x4, 5x5, 6x6,...13x13, and LARGER Dictionaries
    def test_normal_case_3x3(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi", "cfi", "dea"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_normal_case_5x5(self):
        grid = [['qu', 'a', 'x', 'st', 'l'],
                ['a', 'r', 'r', 'i', 'l'],
                ['y', 'f', 'i', 'e', 'd'],
                ['m', 'r', 'i', 'c', 'k'],
                ['a', 'n', 'd', 'm', 'o']]
        dictionary = ['hawaii', 'hero', 'academia', 'army',
                      'ciel', 'derrick', 'still', 'arf']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['arf', 'army', 'ciel', 'derrick', 'still']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)


class TestSuiteSimpleEdgeCases(unittest.TestCase):
    # ADD MANY SIMPLE TEST CASES
    def test_square_grid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # Empty grid
    def test_empty_grid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    # Empty grid and empty dictionary
    def test_empty_grid_and_empty_dict(self):
        grid = []
        dictionary = []
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []
        self.assertEqual(solution, expected)

    # No word in dictionary
    def test_case_no_word_in_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["xyz", "nop"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        self.assertEqual(solution, expected)

    # Repetition of same tiles
    def test_case_with_repeated_tiles(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["aabc", "bcffi", "efhi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["efhi"]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)


class TestSuiteCompleteCoverage(unittest.TestCase):
    # Word that covers the entire grid
    def test_word_that_takes_the_entire_grid(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        # The word "abcdefghi" covers the entire grid in a snake-like manner
        dictionary = ["abcfedghi", "defh", "de"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abcfedghi", "defh"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # Recurse on the diagonal
    def test_diagonal_recursion(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["aei", "cfi", "beh", "abd"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["aei", "cfi", "beh", "abd"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # Test with no adjacent letters in dictionary
    def test_non_adjacent_letters(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["aei", "abc", "ace", "cfg"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "aei"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # Words that are shorter than 3 letters
    def test_short_words(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["ab", "de", "c", "ghi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        # Words shorter than 3 characters should be skipped
        expected = ["ghi"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # Grid that contains Q and S as a single tile
    def test_s_as_single_tiles(self):
        grid = [['a', 'b', 's', 't'],
                ['e', 's', 'e', 'm'],
                ['s', 'n', 'i', 'o'],
                ['s', 'e', 's', 'u']]
        dictionary = ['abstemiousnessesa', 'asbestos',
                      'abstemiousnesses', 'sessensuoimetsba']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        # Because the grid is invalid so the result must be empty
        expected = []
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # Containing double letters tiles (QX where x != u and Sx where x != t)
    def test_double_letters_tiles_other_than_qu_and_st(self):
        grid = [["A", "Qx", "C"],
                ["D", "E", "F"],
                ["p", "H", "I"]]
        dictionary = ["aqxc", "def", "efhi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        # Because the grid is invalid so the result must be empty
        expected = []
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)


class TestSuiteQuAndSt(unittest.TestCase):
    # ADD QU AND ST TEST CASES in single grid
    def test_case_1(self):
        grid = [["Qu", "B"],
                ["St", "D"]]
        dictionary = ["qubd", "stbd", "qust"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["qubd", "stbd", "qust"]
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # ADD QU in grid and ST as a single tile
    def test_case_2(self):
        grid = [["Qu", "A"],
                ["S", "D"]]
        dictionary = ['quac', 'qud', 'a', 'b', 'c', 'qu']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['QUAC', 'QUD', 'QU']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # ADD ST only in grid
    def test_case_3(self):
        grid = [['A', 'B'],
                ['St', 'D']]
        dictionary = ['stbd', 'a', 'b']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['STBD']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # ADD edge case for QU and ST in the same word
    def test_case_4(self):
        grid = [['Q', 'U'],
                ['S', 'T']]
        dictionary = ['qust']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['QSTU']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)

    # ADD edge case for QU and ST not in the same word
    def test_case_5(self):
        grid = [['A', 'B'],
                ['S', 'T']]
        dictionary = ['qu', 'st']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ['QU', 'ST']
        expected = [x.upper() for x in expected]
        solution = sorted(solution)
        expected = sorted(expected)
        self.assertEqual(solution, expected)


if __name__ == '__main__':
    unittest.main()
