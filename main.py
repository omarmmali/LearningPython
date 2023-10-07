import math

class Solution:
    def integerBreak(self, n: int) -> int:
        i, j = 0,0
        answer = -1
        for i in range(0,n):
            for j in range(0, n):
                experiment = (3**i) + (4**j)
                print("the value of i = {i}".format(i))
                print("the value of j = {j}".format(j))
                print("the value of the experiment = {experiment}".format(experiment))
                if i + j < 2:
                    continue
                elif experiment <= n:
                    answer = math.max([experiment, answer])



print(Solution().integerBreak(2))