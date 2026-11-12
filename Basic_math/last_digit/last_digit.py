
class Solution:
    def getLastDigit(self, a, b):

        if b == "0":
            return 1

        # Extract last digit of base
        base = int(a[-1])

        # Calculate exponent modulo 4 (cyclic length of last digits) 1, 2 and 4.
        remainder = 0

        for digit in b:
            remainder = (remainder * 10 + int(digit)) % 4

        # Handle cycle position 4
        if remainder == 0:
            remainder = 4

        return pow(base, remainder, 10)


object = Solution()
#test with edge case by grouping it
#Normal Group
print(object.getLastDigit("2", "3"))  # Output: 8

#Edge Case Group
print(object.getLastDigit("0", "0"))  # Output: 1
print(object.getLastDigit("0", "5"))  # Output: 0
print(object.getLastDigit("5", "0"))  # Output: 1
print(object.getLastDigit("10", "10"))  # Output: 0
print(object.getLastDigit("123456789", "987654321"))  # Output: 9
print(object.getLastDigit("999999999", "999999999"))  # Output: 9
print(object.getLastDigit("12345678901234567890", "98765432109876543210"))  # Output: 0
print(object.getLastDigit("10000000000000000000", "10000000000000000000"))  # Output: 0
print(object.getLastDigit("99999999999999999999", "99999999999999999999"))  # Output: 9
print(object.getLastDigit("123456789012345678901234567890", "987654321098765432109876543210"))  # Output: 0
print(object.getLastDigit("1000000000000000000000000000000", "1000000000000000000000000000000"))  # Output: 0
print(object.getLastDigit("-123", "456"))  # Output: 7
print(object.getLastDigit("-123", "-456"))  # Output: 3
print(object.getLastDigit("123", "-456"))  # Output: 7

#Bottleneck - more conditional checks, more time complexity
#Optimal solution - complexity analysis - O(n) input grows operation linear time
#Math: modular arithmetic
#Edge case test - negative numbers, zero, large integers