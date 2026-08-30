class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashCount = {}
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c)- ord('a')] += 1
            count_tuple = tuple(count)
            if count_tuple in hashCount:
                hashCount[count_tuple].append(string) 
            else:
                hashCount[count_tuple] = [string]
        return list(hashCount.values())