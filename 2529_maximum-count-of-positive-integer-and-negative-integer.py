from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find the first index where nums[index] >= 0
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        
        # The number of negative numbers is 'left'
        neg_count = left
        
        # Find the first index where nums[index] > 0
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        
        # The number of positive numbers is 'len(nums) - left'
        pos_count = len(nums) - left
        
        return max(neg_count, pos_count)
    
    def maximumCount2(self, nums: List[int]) -> int:
        neg_count = bisect_left(nums, 0) 
        pos_count = len(nums) - bisect_left(nums, 1)
        return max(neg_count, pos_count)


sol = Solution()
print(sol.maximumCount([5,20,66,1314]))