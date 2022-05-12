class Solution:
    def hammingWeight(self, n: int) -> int:
        z= bin(n)
        y= str(z)
        print(n)
        return y.count('1')