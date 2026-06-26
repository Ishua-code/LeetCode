# 1652. Defuse the Bomb
# t
# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous -k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []

        if k > 0:
            s = 0
            for i in range(1, k + 1):
                s += code[i]
            res.append(s)

            for i in range(1, n):
                s = s - code[i] + code[(i + k) % n]
                res.append(s)
            return res

        if k == 0:
            for i in range(n):
                res.append(0)
            return res

        if k < 0:
            k = -k
            s = 0
            for i in range(n - k, n):
                s += code[i]
            res.append(s)

            for i in range(1, n):
                s = s - code[(n - k + i - 1) % n] + code[i - 1]
                res.append(s)
            return res