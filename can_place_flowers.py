class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            else:
                print(i)
                if i == 0 and len(flowerbed) > 1:
                    if flowerbed[i + 1] != 1:
                        n -= 1
                        i += 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] != 1:
                        n -= 1
                        i += 1
                else:
                    if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                        n -= 1
                        i += 1
                i += 1

        if n > 0:
            return False

        return True
