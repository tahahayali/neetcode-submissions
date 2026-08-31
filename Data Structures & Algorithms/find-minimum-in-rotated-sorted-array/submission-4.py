class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0], nums[1])
        left, right = 0, n - 1
        m = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] < nums[right]):
                m = min(m, nums[mid])
                right = mid
            else:
                left = mid + 1
        m = min(nums[right], m)
        return m