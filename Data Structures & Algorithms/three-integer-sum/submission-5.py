class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a for loop combined with a two pointer
        # where the two points will be from each edge of the rest
        # of the loop each time
        # calculate the sum of three values each time and if it sums to 0
        # append to the result array
        # deal with duplicate results and base conditions if it exists
        res = []
        n = len(nums)
        nums.sort() # -4, -1, -1, 0, 1, 2

        for i, num in enumerate(nums):
            l = i + 1
            r = n - 1

            if num > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                temp_sum = num + nums[l] + nums[r]
                if temp_sum == 0:
                    res.append([num, nums[l], nums[r]])
                
                if temp_sum > 0:
                    r -= 1
                elif temp_sum < 0:
                    l += 1
                else:
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res