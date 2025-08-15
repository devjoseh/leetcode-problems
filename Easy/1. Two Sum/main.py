# usando hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, i in enumerate(nums):
            if(hash.get(i) is not None):
                return[hash.get(i), index]

            hash[target-i] = index