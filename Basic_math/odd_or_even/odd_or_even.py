class Solution:
    def isEven (self, n):
        return n%2 == 0

obj = Solution()
print(obj.isEven(0))

#Bottle neck
#optimal solution - complexity analysis - O(1) 
#math: modular arithmetic
#edge case test
#usecase - detect a property, cyclic track of a event