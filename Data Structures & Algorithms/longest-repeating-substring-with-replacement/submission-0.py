class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        left = 0
        n = len(s)
        res = 0
        count = {}
        for right in range(n):
            count[s[right]] = 1 + count.get(s[right], 0)
            while ((right - left) + 1 - max(count.values()) > k):
                count[s[left]] -= 1
                left += 1
            res = max(res, (right - left) + 1)
        return res

        