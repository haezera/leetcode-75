class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            for i in range(0, len(str1)):
                copy = str1[:len(str1) - i]
                if self.checkIsDivisor(str2, copy):
                    if self.checkIsDivisor(str1, copy):
                        return copy

            return ""
        elif len(str1) > len(str2):
            for i in range(0, len(str2)):
                copy = str2[:len(str2) - i]
                print(copy)
                if self.checkIsDivisor(str1, copy):
                    if self.checkIsDivisor(str2, copy):
                        return copy
            
            return ""
        else:
            if str1 == str2:
                return str2
            else:
                return ""

    def checkIsDivisor(self, check: str, div: str) -> bool:
        if len(check) % len(div) != 0:
            return False

        multiplier: int = floor(len(check) / len(div))
        temp = ""
        for i in range(0, multiplier):
            temp += div
        
        if temp == check:
            return True
        else:
            return False
