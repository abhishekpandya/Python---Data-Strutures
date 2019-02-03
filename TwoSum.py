## Returns a tuple(i1,i2) where i1 and i2 are the index of numbers whose sum is equal to target

index=0
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target-num] = i