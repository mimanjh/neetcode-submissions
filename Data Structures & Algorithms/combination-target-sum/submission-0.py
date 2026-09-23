class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, calc):
            if calc == target:
                res.append(subset.copy())
                return
            if calc > target or i >= len(nums):
                return

            subset.append(nums[i])
            backtrack(i, calc + nums[i])
            subset.pop()
            backtrack(i + 1, calc)
        
        backtrack(0, 0)
        return res