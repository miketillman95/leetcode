class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        print(int_b)
        summ = int_a + int_b
        bin_summ = bin(summ)
        return bin_summ[2:]
        