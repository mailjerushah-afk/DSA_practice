class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr_count = sum(1 for char in s[:k] if char in vowels)
        maxCount = curr_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_count += 1
            if s[i-k] in vowels:
                curr_count -= 1
            
            if curr_count > maxCount:
                maxCount = curr_count

            if maxCount == k:
                return k
        return maxCount     
