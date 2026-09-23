class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # iterate through from the back
        # iterate forward for each element
        # leave a record of the value
        # get the maximum value for each

        n = len(nums)
        LIS = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
                