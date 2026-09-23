class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # determine if there's a cycle
        adj = collections.defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)

        visited = set()
        visiting = set()
        def dfs(c):
            # if prerequisite already exists in hashMap, return false
            if c in visiting:
                return False
            # otherwise continue
            if c in visited:
                return True

            visiting.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            visiting.remove(c)

            visited.add(c)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
