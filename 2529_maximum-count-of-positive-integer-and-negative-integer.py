from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        
        neg_count = left
        
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        
        pos_count = len(nums) - left
        
        return max(neg_count, pos_count)
    
    def maximumCount2(self, nums: List[int]) -> int:
        neg_count = bisect_left(nums, 0) 
        pos_count = len(nums) - bisect_left(nums, 1)
        return max(neg_count, pos_count)