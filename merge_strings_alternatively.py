class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # First consider the case where there is indeed a remainder
        return_str = ""
        remainder = ""

        if len(word1) < len(word2):
            remainder += word2[len(word1):]
        elif len(word2) < len(word1):
            remainder += word1[len(word2):]
        
        for i in range(0, min(len(word1), len(word2))):
            return_str += word1[i]
            return_str += word2[i]
        
        return_str += remainder

        return return_str
