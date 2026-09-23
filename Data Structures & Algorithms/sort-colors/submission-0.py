class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # bucketSort since 1 <= nums.length <= 300 and 0 <= nums[i] <= 2
        counts = [0] * 3

        for n in nums:
            counts[n] += 1
        
        n = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[n] = i
                n += 1


        