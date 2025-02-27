class Solution(object):
    def isHappy(self, n):
        visit = set() # set'as, kad saugotume unikalias reiksmes

        while n not in visit: # kad isvengti infinite loop'u
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1: 
                return True
        
        return False

    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n % 10
            output += pow(digit, 2)
            n //= 10

        return output
            
