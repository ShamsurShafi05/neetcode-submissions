class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        for i, val in enumerate(nums):
            print(i, val, d1)
            current = val
            need = target-current
            if d1.get(need) != None:
                return sorted([i, d1[need]])
            
            d1[val] = i

