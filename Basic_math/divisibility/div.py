class Solution:
    def divisibleByDigits(self, s):
        count = 0
        l = set(s)

        for i in range(1, 10):

            if str(i) not in l:
                continue

            r = 0

            for digit in s:
                r = ((r * 10) + int(digit)) % i

            if r == 0:
                count += s.count(str(i))

        return count