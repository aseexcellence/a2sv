class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        seen = set()
        while stack:
            room = stack.pop()
            seen.add(room)
            for key in rooms[room]:
                if key not in seen:
                    stack.append(key)
        return len(seen) == len(rooms)