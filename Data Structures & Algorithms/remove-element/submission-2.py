class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                if nums[end] == val:
                    nums[end] = None
                    end -= 1
                else:
                    nums[start] = nums[end]
                    nums[end] = None
                    start += 1
                    end -= 1
            else:
                start += 1
        return len([n for n in nums if n != None])