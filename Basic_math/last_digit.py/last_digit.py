class Solution:
    def last_digit(self, n):
        return n%10


obj = Solution()
value = int(input("Enter a number: "))
print(obj.last_digit(value))