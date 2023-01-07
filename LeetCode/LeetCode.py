from util.LeetCodeUtils import *



s=Solution()
func=s.
paramNumber=str(inspect.signature(func)).count(',')+1
null=None
for case,answer in zip(
[
   
],
[
   
]
):    
    if paramNumber==1:
        res=func(case)
    else:
        res=func(*case)
    print(res==answer,res,answer)