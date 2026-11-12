class Solution:
    def isEven (self, n):
        # Validate input type
        if isinstance(n, bool) or not isinstance(n, int):
            raise TypeError("Input must be an integer")
        
        return n%2 == 0

value = input("Enter a number: ")

try:
    num = int(value)
    obj = Solution()
    print(obj.isEven(num))
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#Bottle neck - more conditional checks, more time complexity
#optimal solution - complexity analysis - O(1) input grows operation constant time
#math: modular arithmetic
#edge case test - negative numbers, zero, large integers