class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = -1
        index2 = -1
        for i in range (0, len(nums)):
            print (i)
            index1 = i
            for j in range (i+1, len(nums)):
                print (j)
                index2 = j
                if nums[i]+nums[j] == target:
                    return [index1, index2]
                else: continue
            
        return [index1, index2]


l = [3,2,4]
test = Solution()

print (test.twoSum(l,6))

