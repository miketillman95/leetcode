class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordconcat1 = "".join(word1)
        wordconcat2 = "".join(word2)
        
        if wordconcat1 == wordconcat2:
            return True
        
        return False