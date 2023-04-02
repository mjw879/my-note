from sortedcontainers import *
from typing import *
from math import *
import math
from collections import *
import collections
from functools import *
import functools
from bisect import *
import bisect
from heapq import *
import heapq
from numpy import *
import numpy as np
from itertools import *
from random import *
import random

import itertools
import inspect

import copy

null=None
true=True
false=False
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printList(head):
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    print(res)
def buildList(l):
    if not l:return None
    head=ListNode(l[0])
    res=head
    for i in l[1:]:
        head.next=ListNode(i)
        head=head.next
    return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def buildTree(nums):
    root=TreeNode(nums[0])
    q=deque([root])
    for i in range(1,len(nums),2):
        head=q.popleft()
        if nums[i]!=null:
            head.left=TreeNode(nums[i])
            q.append(head.left)
        if i+1<len(nums) and nums[i+1]!=null:
            head.right=TreeNode(nums[i+1])
            q.append(head.right)
    return root

def LeetCodeDebug(function,cases,answers):
    paramNumber=function.__code__.co_argcount-1
    for case,answer in zip(cases,answers):
            if paramNumber==1:
                res=function(case)
            else:
                res=function(*case)
            if res!=answer:
                print(res,answer)
            else:
                print()

# 将整型数组arr转换成从start开始的连续的值
# 例：[300,100,200,400] -> [2,0,1,3]
def Narrow(arr,start=0):
    idx={v:i+start for i,v in enumerate(sorted(list(set(arr))))}
    return [idx[i] for i in arr]

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))    # parent[x]表示x的长辈是parent[x]，默认是自己
        self.rank = [0] * n             # rank[x]表示x的辈分,值越大则辈分越高，默认是0

    # 寻找x的长辈(路径压缩)
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 将x和y他们所处的家族合并(启发式合并)
    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1