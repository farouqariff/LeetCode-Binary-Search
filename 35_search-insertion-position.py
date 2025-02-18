from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi :
            mid = lo + (hi-lo)//2
            if nums[mid] < target :
                lo = mid + 1
            elif nums[mid] > target :
                hi = mid - 1
            else :
                return mid
        return lo