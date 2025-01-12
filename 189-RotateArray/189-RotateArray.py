class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) > 1):
            nums.reverse()
            if(k > len(nums)):
                k = k % len(nums)
            l1, r1 = 0, k-1
            l2, r2 = k, len(nums)-1
            while (l1 < r1):
                temp = nums[l1]
                nums[l1] = nums[r1]
                nums[r1] = temp
                l1+=1
                r1-=1
            print(nums)
            while (l2 < r2):
                temp = nums[l2]
                nums[l2] = nums[r2]
                nums[r2] = temp
                l2+=1
                r2-=1