# 区间 DP

## [戳气球](https://leetcode.cn/problems/burst-balloons/)
---
有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。

 

**示例 1：**

    输入：nums = [3,1,5,8]
    输出：167
    解释：
    nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

**示例 2：**

    输入：nums = [1,5]
    输出：10
 

>提示：  
>n == nums.length  
>1 <= n <= 300  
>0 <= nums[i] <= 100


??? tip "思路"

    这题难点在于先选气球会影响后面的相邻关系，导致dp走不下去

    避免这个问题的方法逆向思维，枚举**后选**气球的情况。  
    假如有子状态区间[i,j]，为避免影响后面的相邻关系。我们在本状态中不选择边界。
    假设x（i<x<j）是**最后**一个被戳的，则有状态转移方程  
    $$
    dp[i,j]=max(dp[i,x]+dp[x,j]+nums[k-1]*nums[k]*nums[k+1])
    $$

??? example "示例代码"

    ```python
    class Solution:
        def maxCoins(self, nums: List[int]) -> int:
            nums=[1]+nums+[1]
            @lru_cache(None)
            def f(i,j):
                res=0
                for k in range(i+1,j):
                    res=max(res,f(i,k)+nums[i]*nums[k]*nums[j]+f(k,j))
                return res

            return f(0,len(nums)-1)
    ```



## [合并石头的最低成本](https://leetcode.cn/problems/minimum-cost-to-merge-stones/)
---

有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

 

**示例 1：**

    输入：stones = [3,2,4,1], K = 2
    输出：20
    解释：
    从 [3, 2, 4, 1] 开始。
    合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
    合并 [4, 1]，成本为 5，剩下 [5, 5]。
    合并 [5, 5]，成本为 10，剩下 [10]。
    总成本 20，这是可能的最小值。

**示例 2：**

    输入：stones = [3,2,4,1], K = 3
    输出：-1
    解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.

**示例 3：**

    输入：stones = [3,5,1,2,6], K = 3
    输出：25
    解释：
    从 [3, 5, 1, 2, 6] 开始。
    合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
    合并 [3, 8, 6]，成本为 17，剩下 [17]。
    总成本 25，这是可能的最小值。
 

>提示：  
>1 <= stones.length <= 30  
>2 <= K <= 30  
>1 <= stones[i] <= 100


??? tip "思路"

    **入参k也是子状态**

    假如有n颗石头
    1. 第一个石头可以自成一堆，后面的石头构成k-1堆  
    2. 前k个石头可以成一堆，后面的石头构成k-1堆  
    ...
    3. 前n-k+1个石头可以成一堆，后面预留k-1颗构成k-1堆

    dp[i,j,k]表达[i,j]堆石头中组成k堆的最低成本
    所以有递推公式(其中i!=j)：
    $$
    dp(i,j,1)=
    \begin{cases}
        dp(i,j,k)+sum(stone[i:j+1]), & k=1, \\
        min(f(i,x,1)+f(x+1,j,k-1)), & k>1
    \end{cases}
    $$

??? example "示例代码"

    ```python
    class Solution:
        def mergeStones(self, stones: List[int], k: int) -> int:
            n = len(stones)
            if (n - 1) % (k - 1):  # 无法合并成一堆
                return -1
            s = list(accumulate(stones, initial=0))  # 前缀和

            @cache
            def f(i,j,x):
                if x==1:
                    return 0 if i==j else f(i,j,k)+s[j+1]-s[i]
                res=0xffffffff
                for t in range(i,j,k-1):
                    res=min(res,f(i,t,1)+f(t+1,j,x-1))
                return res
            return f(0,len(stones)-1,1)

    ```