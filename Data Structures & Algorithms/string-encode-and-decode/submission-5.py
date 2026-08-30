class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for string in strs:
            code += str(len(string)) + "#" + string
        return code 


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        "#5hello#5world"
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            result.append(s[i:i+length])
            i += length
        return result
       
