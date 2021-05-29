"""
LC 42: https://leetcode.com/problems/trapping-rain-water/
"""


def trapping_rain_water(height):
    left, right = 0, len(height) - 1
    total_rain_water = 0
    left_max, right_max = 0,0
    while left<right:
        if height[left]<height[right]:
            total_rain_water+=max(left_max,height[left]) - height[left]
            left+=1
        else:
            total_rain_water+=max(right_max,height[right]) - height[right]
            right-=1
    return total_rain_water

