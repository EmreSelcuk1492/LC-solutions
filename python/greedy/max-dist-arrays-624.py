class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        res = 0
        
        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, abs(arr[-1] - minVal), abs(maxVal - arr[0]))
            minVal = min(minVal, arr[0])
            maxVal = max(maxVal, arr[-1])
        return res


# this problem seems simple but I had some issues. You can greedily find the max distance by comparing the curr 
# array values with old max and min but never update the max distance with your own values
# O(n)
