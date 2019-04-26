class Solution:

    def threeSum(self, nums):
        assert len(nums) >= 2

        res = []
        nums.sort()

        for ind in range(len(nums)-2):
            value = nums[ind]
            if value > 0:
                break

            if value == nums[ind-1]:
                continue

            left, right = ind+1, len(nums)-1

            while left < right:
                sum_ = value + nums[left] + nums[right]

                if sum_ < 0:
                    left += 1
                    continue

                if sum_ > 0:
                    right -= 1

                if sum_ == 0:
                    res.append([value, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res


soln = Solution()
out = soln.threeSum([-1, 0, 1, 2, -1, -4])
print(out)

soln = Solution()
out = soln.threeSum([0, 0, 0])
print(out)
