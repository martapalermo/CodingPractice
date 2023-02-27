class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # understand what is pivot index:
        # index where sum of ALL LEFT nums (of index) 
        # is == to sum of ALL RIGHT nums (of index)

        leftSum = 0
        total = sum(nums)
        for i, value in enumerate(nums):
            if leftSum == (total - leftSum - value):
                return i
    
            leftSum += value
        return -1





def main():
    # testcases
    num1 = [1,7,3,6,5,6]
    num2 = [1,2,3]
    num3 = [2,1,-1]

    numlist = [num1, num2, num3]

    for nums in numlist:
        Solution.pivotIndex(Solution, nums)

if __name__ == "__main__":
    main()