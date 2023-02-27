class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # define n for range 
        n = len(nums)
        # initiate runSum arr with value at index 0
        runSum = [nums[0]]

        for i in range (1, n):
            nums[i] += nums[i-1]
            runSum.append(nums[i])
        print(runSum)



def main(): 
    num1 = [1,2,3,4]
    num2 = [1,1,1,1,1]
    num3 = [3,1,2,10,1]
 
    nums = [num1, num2, num3]

    for numbs in nums:
        Solution.runningSum(Solution, numbs)

if __name__ == "__main__":
    main()