class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for ind, val in enumerate(nums):
            indices[val] = ind
        
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in indices and indices[diff] != ind:
                return [ind, indices[diff]]
        return []