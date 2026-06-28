class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        i = 0
        ml = 0

        for j in range(len(s)):

            while s[j] in a:
                a.remove(s[i])
                i += 1

            a.add(s[j])
            ml = max(ml, j - i + 1)

        return ml