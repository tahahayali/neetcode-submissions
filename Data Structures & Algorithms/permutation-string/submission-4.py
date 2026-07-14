class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        count = {}
        res = {}
        left = 0
        for i in range(n):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        for right in range(m):
            if s2[right] in count:
                res[s2[right]] = 1 + res.get(s2[right], 0)

            while (right - left + 1 > n):
                if s2[left] in res:
                    res[s2[left]] -= 1
                left += 1            

            if count == res:
                return True
        return False