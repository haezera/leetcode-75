class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        prefixSum = [0 for i in range(len(nums))]
        total_sum = 0

        for (index, item) in enumerate(nums):
            total_sum += item
            if index == 0:
                prefixSum[0] = 0
            else:
                prefixSum[index] = total_sum

        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = prefixSum[-1] - nums[0]
                if left == right:
                    return 0
            elif i == len(nums) - 1:
                left = prefixSum[-1] - nums[-1]
                right = 0
                if left == right:
                    return len(nums) - 1
            else:
                left = prefixSum[i] - nums[i]
                right = prefixSum[-1] - prefixSum[i]
                if left == right:
                    return i

        return -1
        
