class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_last = s[-1]
        print(s_last)
        
        for i in s:
            print(i)
            if s_last:
                return len(s.split()[-1])
                