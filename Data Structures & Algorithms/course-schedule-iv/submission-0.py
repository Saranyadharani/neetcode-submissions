class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:  #using floyd -warshall
        reachable=[[False]*numCourses for _ in range(numCourses)]
        for prereq,course in prerequisites:
            reachable[prereq][course]=True
        for k in range(numCourses):
            for j in range(numCourses):
                for i in range(numCourses):
                    if reachable[i][k] and reachable [k][j]:
                        reachable[i][j]=True
        return [reachable[u][v]for u,v in queries]