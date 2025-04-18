class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupeDict = {}
        for x in nums:
            if x in dupeDict:
                return True
            else:
                dupeDict[x] = 1
        return False
      # Easy Stoarge - could've used a set instead of a hashMap. good to know the difference 
