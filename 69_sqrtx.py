class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, h = 1, x
        while l <= h:
            mid = l + (h-l)//2
            if x == mid*mid:
                return mid
            elif x < mid*mid:
                h = mid - 1
            else:
                l = mid + 1
        return h

sol = Solution()
print(sol.mySqrt(8))