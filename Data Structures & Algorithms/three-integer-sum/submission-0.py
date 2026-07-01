class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s_nums = sorted(nums)
        res = []
        for k in range(n):
            left = k + 1
            right = n - 1
            while left < right:
                if (s_nums[k] + s_nums[left] + s_nums[right] < 0):
                    left += 1
                elif (s_nums[k] + s_nums[left] + s_nums[right]) > 0:
                    right -= 1
                else:
                    sol = [s_nums[k], s_nums[left], s_nums[right]]
                    if sol not in res:
                        res.append(sol)
                    left += 1
                    right -= 1
        return res
                
                