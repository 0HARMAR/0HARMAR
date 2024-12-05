class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(len(nums)):
            find_add = target-nums[j]
            for i in range(len(nums)-1):
                if nums[i] == find_add:
                    return [j,i]
