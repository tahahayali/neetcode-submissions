class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        curr = set()
        res = 1
        n = len(s)
        for right in range(n):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            res = max(res, (right - left) + 1)
        return res