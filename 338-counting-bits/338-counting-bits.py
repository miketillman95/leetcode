class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        
        for n in range(num + 1):
            print(num+1)
            
            result.append(int(bin(n)[2:].count('1')))
        return result