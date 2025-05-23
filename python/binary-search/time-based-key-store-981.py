class TimeMap:

    def __init__(self):
       self.time_map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = list()
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        curr_list = self.time_map[key]
        l, r = 0, len(curr_list)
        result = 0
        while l < r:
            mid = (l+r) // 2
            if curr_list[mid][0] == timestamp:
                return curr_list[mid][1]
            elif curr_list[mid][0] > timestamp:
                r = mid-1
            else:
                result = mid
                l = mid+1
        if curr_list[result][0] >  timestamp:
            return ""
        if r < len(curr_list) and curr_list[r][0] == timestamp:
            return curr_list[l][1]
        return curr_list[result][1]









# here is a cleaner binary search template for finding the greatest val less than value youre looking for
left, right = 0, len(self.data[key]) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if self.data[key][mid][0] <= timestamp:
                # assign to result every time it's valid while searching
                result = mid
                left = mid + 1
            else:
                right = mid - 1
            
        # if we found a result, it'll be the largest value <= timestamp
        # if not, return ""
        if result == -1:
            return ""
        else:
            return self.data[key][result][1]
