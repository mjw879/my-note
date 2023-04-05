# 动态规划基础

## [最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/)
给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
 
**示例 1：**  
    输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]  
    输出：3  
    解释：长度最长的公共子数组是 [3,2,1] 。

**示例 2：**  
    输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]  
    输出：5
 
>提示：  
>1 <= nums1.length, nums2.length <= 1000  
>0 <= nums1[i], nums2[i] <= 100

??? tip "思路"

    TODO    

??? example "示例代码"

    ```python
    class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for _ in nums2] for _ in nums1]
        res=0
        for i in range(len(nums2)):
            if nums1[0]==nums2[i]:
                dp[0][i]=1
                res=max(res,dp[0][i])
        for i in range(len(nums1)):
            if nums1[i]==nums2[0]:
                dp[i][0]=1
                res=max(res,dp[i][0])
        
        for i in range(1,len(nums1)):
            for j in range(1,len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                    res=max(res,dp[i][j])
                    
        return res
    ```


## [最短公共超序列](https://leetcode.cn/problems/shortest-common-supersequence/)
---
√

给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。

（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）

 

**示例：**

    输入：str1 = "abac", str2 = "cab"
    输出："cabac"
    解释：
    str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
    str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
    最终我们给出的答案是满足上述属性的最短字符串。
     

>提示：  
>1 <= str1.length, str2.length <= 1000  
>str1 和 str2 都由小写英文字母组成。


??? tip "思路"

    求最短公共子序列    


??? example "示例代码"

    ```python
    class Solution:
        def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
            @lru_cache(None)
            def getSCS(i,j):
                if i==len(str1) or j==len(str2):
                    return ""
                res=""
                if str1[i]==str2[j]:
                    res=str1[i]+getSCS(i+1,j+1)
                t1,t2=getSCS(i,j+1),getSCS(i+1,j)
                if len(res)<len(t1):
                    res=t1
                if len(res)<len(t2):
                    res=t2
                return res
            SCS=getSCS(0,0)
            i,j,x=0,0,0
            res=""
            while i<len(str1) or j<len(str2):
                if x==len(SCS):
                    res+=str1[i:]+str2[j:]
                    break
                else:
                    ii,jj=i,j
                    while SCS[x]!=str1[ii]:
                        ii+=1
                    while SCS[x]!=str2[jj]:
                        jj+=1
                    res+=str1[i:ii]+str2[j:jj]+SCS[x]
                    i=ii+1
                    j=jj+1
                    x+=1
            return res
    ```


## [无矛盾的最佳球队](https://leetcode.cn/problems/best-team-with-no-conflicts/)
---
√

假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。

然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。

给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队中得分最高那支的分数 。

 

**示例 1：**

    输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
    输出：34
    解释：你可以选中所有球员。

**示例 2：**

    输入：scores = [4,5,6,5], ages = [2,1,2,1]
    输出：16
    解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。

**示例 3：**

    输入：scores = [1,2,3,5], ages = [8,9,10,1]
    输出：6
    解释：最佳的选择是前 3 名球员。
 

>提示：  
>1 <= scores.length, ages.length <= 1000  
>scores.length == ages.length  
>1 <= scores[i] <= 106  
>1 <= ages[i] <= 1000  



??? tip "思路"

    *这是一道需要优化才不会超时的动态规划题*

    先按年龄和分数排序  
    假设dp[i][j]是从i开始选择，上一个选择的是j的最佳无矛盾球员选择，则：  

    $$
    dp[i][j]=
    \begin{cases}
        max(dp[i+1][j],dp[i+1][i]+scores[i]) & , ages[i]=ages[j] \\
        dp[i+1][j] & , ages[j]<ages[i],scores[j]{\le}scores[i]
    \end{cases}
    $$
    
    如果选了i，那就要**直接**向右遍历到$ages[j]<ages[i],scores[j]{\le}scores[i]$的情况，在做选择（减枝，而不是一个一个选）

    同类型题：[最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

??? example "示例代码"

    ```python
    class Solution:
        def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
            t=[[0,0]]+list(sorted(zip(ages,scores)))
            def check(i,j):
                return t[i][0]==t[j][0] or t[i][1]<=t[j][1]

            @cache
            def f(i):
                if i==len(t):
                    return 0
                res=0
                for j in range(i+1,len(t)):
                    if check(i,j):
                        res=max(res,f(j))
                return res+t[i][1]
            return f(0)
    ```
