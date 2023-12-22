class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k - 1
        max_sum = 0
        curr_sum = 0
        for i in range(l, r + 1):
            max_sum += nums[i]
        max_value = max_sum / k
        curr_sum = max_sum 
        curr_value = curr_sum / k
        l += 1
        r += 1

        while r < len(nums):
            curr_sum -= nums[l - 1]
            curr_sum += nums[r]

            curr_value = curr_sum / k

            if curr_value > max_value:
                max_value = curr_value
            
            l += 1
            r += 1

        return max_value
