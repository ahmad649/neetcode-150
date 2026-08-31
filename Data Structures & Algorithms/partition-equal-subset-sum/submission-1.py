class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            dpNext = dp.copy()
            for val in dp:
                dpNext.add(val + nums[i])
                if val + nums[i] == target:
                    return True

            dp = dpNext
        return False