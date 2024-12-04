class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {} # needed, index

        for index, value in enumerate(nums):
            needed = target - value

            if needed in num_map:
                return [num_map[needed], index]

            num_map[value] = index
            
            
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))