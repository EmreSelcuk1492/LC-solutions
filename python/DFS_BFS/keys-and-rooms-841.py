# a dfs problem where we want to visit every room
# edge cases: if room zero has no key, then doesnt work unless only one room

# want to keep track of what rooms we haven't visited
# want to keep track of what keys we have 
# in each room we iterate over all keys and add them to our curr list of keys
# can do this with bfs


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = deque()
        q.append(0)
        while len(q) > 0:
            qlen = len(q)
            for i in range(qlen):
                curr_room = q.popleft()
                curr_arr = rooms[curr_room]
                for key in curr_arr:
                    if key not in visited:
                        visited.add(key)
                        q.append(key)
        return len(visited) == len(rooms)
           
# runtime: O(N+K)



# DFS solution
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(curr_room, rooms, visited):
            if curr_room in visited:
                return
            visited.add(curr_room)
            for key in rooms[curr_room]:
                dfs(key, rooms, visited)
            return
        visited = set()
        dfs(0, rooms, visited)
        return len(visited) == len(rooms)


