class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_score = 10**5
        for i in range(len(nums) - k + 1):
            min_score = min(min_score, nums[i + k - 1] - nums[i])
        return min_score