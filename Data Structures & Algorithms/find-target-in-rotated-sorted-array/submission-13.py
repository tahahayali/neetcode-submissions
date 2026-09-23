class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            # Means we're on left side
            if (nums[left] <= nums[mid]):
                # Means target is on left side, dismiss the right
                if (target < nums[mid] and target > nums[left]):
                    right = mid
                else:
                    left = mid + 1
            # Means we're on right side
            else:
                # Means target is on the right side, dismiss left
                if (nums[mid] < target and target < nums[right]):
                    left = mid
                else:
                    right = mid - 1

        return -1
            