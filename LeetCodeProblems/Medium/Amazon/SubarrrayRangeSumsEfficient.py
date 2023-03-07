"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from typing import List

def subArrayRanges(nums: List[int]) -> int:
    total = 0
    for i in range(len(nums)):
        min_v = max_v = nums[i]
        for j in range(i + 1, len(nums)):
            min_v = min(nums[j], min_v)
            max_v = max(nums[j], max_v)

            total += max_v - min_v
    print (total)

def main():
    testCases = [
        [1,2,3], [1,3,3], [4,-2,-3,4,1]
    ]

    # [1,2,3] --> Output: 4
        # Explanation: The 6 subarrays of nums are the following:
        # [1], range = largest - smallest = 1 - 1 = 0 
        # [2], range = 2 - 2 = 0
        # [3], range = 3 - 3 = 0
        # [1,2], range = 2 - 1 = 1
        # [2,3], range = 3 - 2 = 1
        # [1,2,3], range = 3 - 1 = 2
        # So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

    # [1,3,3] --> Output: 4 

    # [4, -2, -3, 4, 1] --> Output: 59
 
    for case in testCases:
        subArrayRanges(case)

if __name__ == "__main__":
    main()