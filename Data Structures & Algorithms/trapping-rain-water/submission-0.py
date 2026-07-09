class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxLeft = height[left]
        maxRight = height[right]
        total = 0
        while left <= right:
            if maxLeft <= maxRight:
                total += max(0, (maxLeft - height[left]))
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                total += max(0, (maxRight - height[right]))
                maxRight = max(maxRight, height[right])
                right -= 1

        return total

        