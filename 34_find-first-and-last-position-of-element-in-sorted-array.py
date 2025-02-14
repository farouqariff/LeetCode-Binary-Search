from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)-1
        return [self.st_pos(nums, target, lo, hi),self.en_pos(nums, target, lo, hi)]

    def st_pos(self, nums, target, lo, hi):
        lo, hi = 0, len(nums) - 1
        first_pos = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:  # Move right
                lo = mid + 1
            else:  # target <= nums[mid], move left
                hi = mid - 1
            if target == nums[mid]:  # Store the possible first position
                first_pos = mid  
        return first_pos
    
    def en_pos(self, nums, target, lo, hi):
        lo, hi = 0, len(nums) - 1
        last_pos = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target < nums[mid]:  # Move left
                hi = mid - 1
            else:  # target >= nums[mid], move right
                lo = mid + 1
            if target == nums[mid]:  # Store the possible last position
                last_pos = mid  
        return last_pos

sol = Solution()
print(sol.searchRange([5,7,7,8,8,10],8))
