class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 1 or k == 0:
            return
        if k > len(nums):
            k = k%len(nums)
        front_list = nums[-k:]
        back_list = nums[:len(nums)-k]
        for i in range(len(front_list)):
            nums[i] = front_list[i]
        for j in range(len(back_list)):
            nums[j+len(front_list)] = back_list[j]
