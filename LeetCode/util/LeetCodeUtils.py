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