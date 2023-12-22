class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrHashMap = collections.defaultdict(int)

        for i in arr:
            arrHashMap[i] += 1
        
        valuesList = []
        set_arr = list(set(arr))
        for i in set_arr:
            valuesList.append(arrHashMap[i])
        print(valuesList)
        if len(valuesList) != len(list(set(valuesList))):
            return False
        
        return True
