from collections import deque


class Solution:

    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        if k == 0:
            return nums

        deq = deque()
        deq2 = deque()
        result = []

        for i in range(k):
            while len(deq) != 0:
                print(nums[i], deq[-1])
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                    deq2.pop()
                else:
                    break

            deq.append(i)
            deq2.append(nums[i])

        print(deq2)

        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            if deq[0] < i - k + 1:
                deq.popleft()
                deq2.popleft()

            while len(deq) != 0:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                    deq2.pop()
                else:
                    break

            deq.append(i)
            deq2.append(nums[i])
            print(deq2)

        result.append(nums[deq[0]])

        return result


soln = Solution()
out = soln.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(out)
