# class Solution:
#     def romanToInt(self, s: str) -> int:

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# The HINT says it's easy to solve if you work the string from back to front and use a map() function 
#
# can also use enumerate
# 
# Store the values of the roman numerals in a dictionary?
# [start:stop:step]

class Solution:
    def __init__(self):
        self.numerals = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                    }

    def romantoInt(self,s):
        self.s = s
        total = 0
        revs = self.s[::-1]
        y = []
        for x in revs:
            y.append(self.numerals[x])
            total = total + self.numerals[x]
            if len(y) >= 2:
                if (y[-1] == 1 and y[-2] == 5):
                    total = total - 2
                elif (y[-1] == 1 and y[-2] == 10):
                    total = total - 2
                elif (y[-1] == 10 and y[-2] == 50):
                    total = total - 20
                elif (y[-1] == 10 and y[-2] == 100):
                    total = total - 20
                elif (y[-1] == 100 and y[-2] == 500):
                    total = total - 200
                elif (y[-1] == 100 and y[-2] == 1000):
                    total = total - 200
        return total
        
input = 'IV'
c = Solution()
results = c.romantoInt(input)
print("The number is " + str(results) + "!")
