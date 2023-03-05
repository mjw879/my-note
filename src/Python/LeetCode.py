from util.LeetCodeUtils import *

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        c=Counter([i&j for i in nums for j in nums])

        res=0
        for i in nums:
            t=~i&0xfffffff
            res+=c[i]
        return res


s=Solution()
func=s.countTriplets
paramNumber=str(inspect.signature(func)).count(',')+1
null=None
for case,answer in zip(
[
   [2,1,3]
],
[
   12
]
):    
    if paramNumber==1:
        res=func(case)
    else:
        res=func(*case)
    print(res==answer,res,answer)