class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                three_sum = a + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res