from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a graph and create a indegree for tracking courses and prereq
        graph={i :[] for i in range (numCourses)} 
        indegree=[0]*(numCourses)
        for course,prereq in prerequisites: # creating the indegree
            graph[prereq].append(course)
            indegree[course]+=1
        
        queue=deque([i for i in range(numCourses)  if indegree[i]==0])
        count=0

        while queue:
            node=queue.popleft()
            count+=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)

        return count==numCourses
        
