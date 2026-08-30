class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        longest = 0
        hashset = set()

        while (right < len(s)):
            if s[right] not in hashset:
                hashset.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                hashset.remove(s[left])
                left += 1
        return longest