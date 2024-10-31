class Solution:
    def trap(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water

# Example usage:
sol = Solution()
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol.trap(height1))  # Output: 6

height2 = [4, 2, 0, 3, 2, 5]
print(sol.trap(height2))  # Output: 9