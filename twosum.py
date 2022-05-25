import itertools
from typing import List

def twoSum(intList: List[int], target: int) -> List[int]:
    for nums in itertools.combinations(intList, 2):
        if sum(nums) == target:
            print([intList.index(number) for number in nums])

def main():
    intList = [2,7,11,15] 
    target = 9

    twoSum(intList, target)

if __name__ == "__main__":
        main()