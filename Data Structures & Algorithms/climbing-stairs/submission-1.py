class Solution:
    def climbStairs(self, n: int) -> int:
        """
        thi is a dynamic programming problm so I want to break it into pieces. 
        what's the smallest bit I can solve?
        What is the repetitive piece?
        How can I frame it into recursive problem

        1. step 1 - 1 step 2 - 2 ways
        2. Step 3 - (step (3-1) )+ (step (3-2))
        3. Step n = step n-1 + Step n-2
        """

        if n == 1:
            return 1
        elif n == 2: 
            return 2
        else:
            numOfWays = [1, 2]
            for i in range(3,n+1):
                  numOfWays.append(numOfWays[i-1-1]+numOfWays[i-2-1])
            return numOfWays[n-1]