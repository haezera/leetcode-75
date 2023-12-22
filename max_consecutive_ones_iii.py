class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        numberOfZeroes = 0
        l = 0
        r = len(nums) - 1

        # Count the number of zeroes in the initial sliding window
        for i in nums:
            if i == 0:
                numberOfZeroes += 1
            
        while numberOfZeroes > k and r > 0:
            if nums[r] == 0:
                numberOfZeroes -= 1
            
            r -= 1
        if r == l and numberOfZeroes > k:
            maxLen = 0
        else:
            maxLen = r - l + 1
        # Now we have the biggest subarray currently, from the start.
        # Our goal is to now slide this window, and extend it as 
        # much as possible, until the window reaches the end. 

        while r < len(nums) - 1:
            print(l, r)
            # Make a movement, and then check if we broke a rule.
            r += 1
            if nums[r] == 0:
                numberOfZeroes += 1
            
            # Now check if we have too many zeroes.
            if numberOfZeroes > k:
                # Increment until number of zeroes  == k
                while numberOfZeroes > k and l != r:
                    l += 1
                    if nums[l - 1] == 0:
                        numberOfZeroes -= 1

            # After all that, check the length of the subarray now.
            if r != l or numberOfZeroes <= k:
                maxLen = max(maxLen, r - l + 1)

        return maxLen
