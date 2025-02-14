from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            missing = arr[mid] - (mid + 1)  # Correct way to count missing numbers

            if missing < k:
                lo = mid + 1  # Search right
            else:
                hi = mid - 1  # Search left

        # After binary search, the kth missing number is: 
        return lo + k  # `lo` is the number of non-missing elements
