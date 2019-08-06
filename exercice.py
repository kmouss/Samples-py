class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        updatedList = [ ]
        updatedList.append(nums[0])
        previous = updatedList[0]
        for i in range(1, len(nums)):
            print ("i={0}, previous = {1}, nums[i] = {2}", i, previous, nums[i])
            if (nums[i] == previous): 
                continue
            else:
                updatedList.append(nums[i])
                previous = nums[i]                
            print nums
            print updatedList   
        nums = updatedList[:]
        print nums
        return len(nums)


l = [1,1,1,2, 2, 3, 3]
test = Solution()
print test.removeDuplicates(l)

print l