class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0 for i in range(len(gain))]
        gain_sum = 0
        for (index, value) in enumerate(gain):
            if index == 0:
                prefix_sum[0] = 0
                gain_sum += value
            else:
                gain_sum += value
                prefix_sum[index] = gain_sum
        min_prefix = max(prefix_sum)
        return max(min_prefix, gain[0])
