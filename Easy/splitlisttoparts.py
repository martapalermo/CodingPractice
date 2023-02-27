# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# NOTE: this file implementation doesnt seem to work and throws attributeError for the .next 
#       implementation however works on leetcode ide and passes all testcases.
#       Trying to figure out this issue -- will commit fixed update 

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        # figure out how many elements are in the listNode 
        curr = head 
        length = 0
        while curr: 
            curr = curr.next
            length += 1
        
        # use mod operator or divmod to figure out division and remainders:
        # if % result is == 0, we can split the head in k equal parts 
        # if % result is == 1, we have one remainder, so one part won't be equal (ex 2 provided)
        # if % result is > 1, we will add null nodes [[],[],[]]
        curr = head 
        result = [] 
        q, r = divmod(length, k)
        for i in range(k):
            temp = curr
            for j in range(q + (i<r) - 1):
                curr = curr.next 
            if curr:
                x = curr.next
                curr.next = None 
                curr = x
            result.append(temp)
        return result


def main():
    # testcases
    head1 = [1,2,3] 
    k1 = 5

    head2 = [1,2,3,4,5,6,7,8,9,10]
    k2 = 3

    Solution.splitListToParts(Solution, head1, k1)
    Solution.splitListToParts(Solution, head2, k2)

if __name__ == "__main__":
    main()