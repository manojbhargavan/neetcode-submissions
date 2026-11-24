class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        number_of_cones = 0
        maxes = 0
        for i in nums:
            if i == 1:
                number_of_cones = number_of_cones + 1
            else:
                maxes = max(maxes, number_of_cones)
                number_of_cones = 0
        maxes = max(maxes, number_of_cones)
        return maxes