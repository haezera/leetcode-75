class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        sub_res1 = []
        sub_res2 = []
        nums1_hmap = collections.defaultdict(bool)
        nums2_hmap = collections.defaultdict(bool)

        for i in nums1:
            nums1_hmap[i] = True
        
        for i in nums2:
            nums2_hmap[i] = True

        for i in nums1:
            if nums2_hmap[i] == False:
                sub_res1.append(i)

        for i in nums2:
            if nums1_hmap[i] == False:
                sub_res2.append(i)

        set_subres = set(sub_res1)
        res.append(list(set_subres))
        set_subres = set(sub_res2)
        res.append(list(set_subres))

        return res
