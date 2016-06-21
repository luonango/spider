#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
import random


# http://blog.csdn.net/handsomekang/article/details/41346645
# 时间复杂度:O(n).
def qselect(A, k):
    if len(A) < k:
        return A
    pivot = A[-1]
    right = [pivot] + [x for x in A[:-1] if x[1] >= pivot[1]]
    rlen = len(right)
    print pivot, right, rlen
    if rlen == k:
        return right
    if rlen > k:
        return qselect(right, k)
    else:
        left = [x for x in A[:-1] if x[1] < pivot[1]]
        return qselect(left, k - rlen) + right


print qselect([["f8505", 1], ['8345', 13], ['82305', 21], ['55', 19], ['857', 10]], 3)

# for i in range(1, 10):
#     print qselect([11, 8, 4, 1, 5, 2, 7, 9], i)
#
# # 给出N长的序列，求出TopK大的元素，使用小顶堆，heapq模块实现。
# class TopkHeap(object):
#     def __init__(self, k):
#         self.k = k
#         self.data = []
#
#     def Push(self, elem):
#         if len(self.data) < self.k:
#             heapq.heappush(self.data, elem)
#         else:
#             topk_small = self.data[0]
#             if elem[1] > topk_small[1]:
#                 heapq.heapreplace(self.data, elem)
#
#     def TopK(self):
#         return [x for x in reversed([heapq.heappop(self.data) for x in xrange(len(self.data))])]
#
#
# if __name__ == "__main__":
#     print "Hello"
#     list_rand = random.sample(xrange(10000), 100)
#     print list_rand
#     list_rand = [[8505, 1], [8345, 13], [82305, 21], [55, 19], [857, 10]]
#     th = TopkHeap(k=3)
#     for i in list_rand:
#         th.Push(i)
#     top = th.TopK()
#     print top
#
#     print sorted(top, reverse=True)
