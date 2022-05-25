# import itertools
from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print("[%d,%d]" % (i, j))
              

    # for nums in itertools.combinations(intList, 2):
    #     if sum(nums) == target:
    #         print([intList.index(number) for number in nums])

def main():
    # testcase 1
    intList = [2,7,11,15] 
    target = 9

    print("Expected: [0,1]")
    twoSum(intList, target)

    # testcase 2
    intList1 = [3,3]
    target1 = 6
       
    print("\nExpected: [0,1]")
    twoSum(intList1, target1)

    # testcase 3
    intList2 = [3,2,4]
    target2 = 6

    print("\nExpected: [1,2]")
    twoSum(intList2, target2)
    
if __name__ == "__main__":
        main()