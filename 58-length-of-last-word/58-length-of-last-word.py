class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_last = s[-1]
        print(s_last)
        if s_last:
            return len(s.split()[-1])
