class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = []
        for ind, num in enumerate(nums):
            nums2.append([num, ind])
        nums2.sort()

        left = 0
        right = len(nums2) - 1
        while (left < right):
            if nums2[left][0] + nums2[right][0] == target:
                return sorted([nums2[left][1], nums2[right][1]])
            elif nums2[left][0] + nums2[right][0] > target:
                right -= 1
            else:
                left += 1
        
        return []

        