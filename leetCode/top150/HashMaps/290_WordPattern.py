class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c

        return True 

        # Time: O(n), n is the number of words in s (or pattern)
        # Memory: O(n), worst case scenario both hashmaps map for
        # every char in pattern and every word in s, which is n 