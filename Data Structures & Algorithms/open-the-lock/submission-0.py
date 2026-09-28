class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #create a set for the deadends
        dead=set(deadends)
        #check if the initial lock 0000 is also a deadend /not
        if "0000" in dead:
            return -1
        #add the intial lock to the queue
        queue=deque([("0000",0)])
        visited={"0000"}
        while queue:
            lock,turns=queue.popleft()
            for i in range(4):
                 #represents the 4 digits
                 for d in (-1,1):
                    new_digit=(int(lock[i])+d)%10
                    new_lock=lock[:i]+str(new_digit)+lock[i+1:]
                    if new_lock not in visited and new_lock not in dead:
                        visited.add(new_lock)
                        queue.append((new_lock,turns+1))
            if lock==target:
                return turns
                
        return -1
