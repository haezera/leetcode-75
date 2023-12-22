class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Two main cases:
        # 1. The longest string contains a single zero
        # 2. The longest string contains no zeroes.
        # Both of these cases are fine. So our conditions should account for both of these scenarios.

        # First count the zeroes present
        numOfZeroes = 0
        for i in nums:
            if i == 0:
                numOfZeroes += 1

        l = 0
        r = len(nums) - 1
        
        while numOfZeroes > 1:
            if nums[r] == 0:
                numOfZeroes -= 1
            r -= 1

        # We will have to remove one from this later.
        maxSubArray = r - l + 1

        while r < len(nums) - 1:
            r += 1
            if nums[r] == 0:
                numOfZeroes += 1
            
            while numOfZeroes > 1 and l != r:
                l += 1
                if nums[l - 1] == 0:
                    numOfZeroes -= 1

            maxSubArray = max(maxSubArray, r - l  + 1)

        return maxSubArray - 1

