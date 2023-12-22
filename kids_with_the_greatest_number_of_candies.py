class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False for i in range(len(candies))]
        for (i, item) in enumerate(candies):
            if item + extraCandies >= max(candies):
                res[i] = True

        return res
