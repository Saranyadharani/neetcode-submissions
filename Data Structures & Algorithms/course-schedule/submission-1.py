from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i :[] for i in range (numCourses)}  #create a graph
        indegree=[0]*(numCourses) # create a indegree list of length of numCourses
        for course,prereq in prerequisites: # creating the indegree
            graph[prereq].append(course) # map the preq -> course
            indegree[course]+=1 #increment corresponding course's indegree by 1
        
        queue=deque([i for i in range(numCourses)  if indegree[i]==0]) # add the course to the queue which has 0 prereq
        count=0 # INTIALIZE THE COUNT TO 0

        while queue: # when there are node to process in the queue is left
            node=queue.popleft() #pop it out and increment the count
            count+=1
            for neighbor in graph[node]: #check for its neighbor decrement its indegree when the indegree becomes zero add it to the queue
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)

        return count==numCourses # return True if the  count == numCourses
        
