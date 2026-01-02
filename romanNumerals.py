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
