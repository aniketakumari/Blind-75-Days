class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prem = {}

        for i, n in enumerate(nums):
            if target - n in prem:
                return ([prem[target - n], i])
            elif n not in prem:
                prem[n] = i
