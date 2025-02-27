# 1st method, the easier one
class Solution(object):
    def isPalindrome(self, s):
        newStr = ""

        for c in s:
            if c.isalnum(): # check if it's alphanumeric
                newStr += c.lower() # convert to lowerCase and add to string
        # check if matches the reversed string, returns true in that case
        return newStr == newStr[::-1]

        
# 2nd method, without the built-in libraries and without using extra memory, O(1) memory
class Solution(object):
    def isPalindrome(self, s):
        l,r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True
    
    # helper function - takes a single character and determines if it's alphaNumeric
    def alphaNum(self, c):
        # if alphaNumeric - returns true, else - false
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord ('9'))


