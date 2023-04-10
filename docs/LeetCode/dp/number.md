# 数位DP

## [至少有 1 位重复的数字](https://leetcode.cn/problems/numbers-with-repeated-digits/submissions/)
---
给定正整数 n，返回在 [1, n] 范围内具有 至少 1 位 重复数字的正整数的个数。
 
**示例 1：**

    输入：n = 20
    输出：1
    解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

**示例 2：**

    输入：n = 100
    输出：10
    解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

**示例 3：**

    输入：n = 1000
    输出：262
 
>提示：  
>1 <= n <= 109  

??? tip "思路"

    有状态`dp(i,limit,choice)`  
    其中`i`表示第`i`位  
    `limit`表示前`i-1`位是否跟`n`的前`i-1`位一样  
    `choice`表示前面是否选择过  

??? example "示例代码"

    ```python
    class Solution:
        def numDupDigitsAtMostN(self, n: int) -> int:
            n=str(n)
            @cache
            def f(i,limit,choice):
                if i==len(n):
                    return int(choice)
                t=0
                if not choice:
                    for x in range(1,10):
                        t+=f(i+1,False,True)
                    return t+f(i+1,False,False)
                else:

                    if limit:
                        for x in range(int(n[i])):
                            t+=f(i+1,False,True)
                        return f(i+1,True,True)+t
                    else:
                        for x in range(10):
                            t+=f(i+1,False,True)
                        return t
            return f(0,True,True)+f(0,False,False)
    ```

