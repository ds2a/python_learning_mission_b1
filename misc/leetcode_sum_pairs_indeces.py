# class Solution:
#     def twoSum(self, nums, target):
#         result = []
#         for first_num in nums:
#             pair_number = target - first_num
#             search_index_start_position = nums.index(first_num)
#             if pair_number in nums[search_index_start_position:]:
#                 result.append((nums.index(first_num), nums.index(pair_number)))
#         return  result
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen = {}
        for first_num in nums:
            pair_number = target - first_num
            search_index_start_position = nums.index(first_num) + 1
            if pair_number in nums[search_index_start_position:]:
                result.append(nums.index(first_num))

                result.append(nums[search_index_start_position:].index(pair_number))
        return  result


# nums = [2,7,11,15]
nums = [3,3]
# target = 9
target = 6

s = Solution()
print(s.twoSum(nums,target))




