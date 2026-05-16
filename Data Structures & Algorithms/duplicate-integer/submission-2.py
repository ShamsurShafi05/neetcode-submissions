class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i, val in enumerate(nums):
            if count.get(val) == None:
                count[val] = 0
            else:
                count[val] += 1
                return True
            
        return False

        