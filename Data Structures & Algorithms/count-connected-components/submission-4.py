class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create a adjacency list
        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=set() # to keep track of the node which has been visited/or not
        count=0 #set the counter to 0 intially
        for i in range(n):
            if i not in visited:
                count+=1
                queue=deque([i])
                visited.add(i)
                while queue:
                    node=queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        return count
