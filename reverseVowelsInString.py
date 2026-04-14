class Solution:
    def reverseVowels(self, s: str) -> str:
        vowls = set("aeiouAEIOU")
        s = list(s)

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowls:
                left +=1 
                continue
            if s[right] not in vowls:
                right -= 1
                continue
            
            s[left], s[right] = s[right], s[left]
            left +=1 
            right -=1

        return "".join(s)

        