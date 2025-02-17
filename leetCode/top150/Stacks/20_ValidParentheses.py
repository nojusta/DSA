class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for c in s:
            # checks if c is a closing bracket
            if c in closeToOpen: 
                # checks if the stack is not empty and matches the maps opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            # if c is an opening bracket, add it to the stack
            else:
                stack.append(c)
        # if the stack is empty return true, else false
        return True if not stack else False
        
# Time: O(n), where n is the characters in string
# Memory: O(n), because of the stack potentially be up to the amount of characters in s