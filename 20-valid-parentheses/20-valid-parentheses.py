class Solution(object):
    def isValid(self, s):
        
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", '').replace("[]", "")
        print(s)
            
        return s == ""
        
            
        
        
        """
        :type s: str
        :rtype: bool
        """
        