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
# can also use enumerate
#
# This was the first attempt that felt very rough and grindy? Just felt like the operations could be done
# by some form of in built functions

class Solution:
    def romanToInt(self,s):
        self.s = s
        y = 0      
        x = 0
        z = x - 1
        storage = []
        while x <= len(self.s):
            if x == 'M':
                if storage[z] == 'I':
                    y = y + 900
                y = y + 1000
            elif x=='D':
                y = y + 500
            elif x=='C':
                y == y + 100
            elif x == 'L':
                y = y + 50
            elif x == 'X':
                y = y + 10
            elif x == 'V':
                y = y + 5
            elif x == 'I':
                y = y + 1
            storage.append(x)
        return y,self.s,storage

c = Solution()
result = c.romanToInt('LLIX')
print(result)
