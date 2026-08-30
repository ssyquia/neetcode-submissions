class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        longest = 1
        current = 1
        
        for i in range(1, len(nums)):
            # Skip duplicates - they don't break the sequence
            if nums[i] == nums[i-1]:
                continue
            # If consecutive, extend current sequence
            elif nums[i] == nums[i-1] + 1:
                current += 1
            # Otherwise, reset the count
            else:
                current = 1
            
            longest = max(longest, current)
        
        return longest