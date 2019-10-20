"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


Approach 1: Brute Force
Intuition & Algorithm

Traverse all the linked lists and collect the values of the nodes into an array.
Sort and iterate over this array to get the proper value of nodes.
Create a new sorted linked list and extend it with the new nodes.
As for sorting, you can refer here for more about sorting algorithms.


Complexity Analysis

Time complexity : O(N log N)O(NlogN) where NN is the total number of nodes.

Collecting all the values costs O(N)O(N) time.
A stable sorting algorithm costs O(N log N)O(NlogN) time.
Iterating for creating the linked list costs O(N)O(N) time.
Space complexity : O(N)O(N).

Sorting cost O(N)O(N) space (depends on the algorithm you choose).
Creating a new linked list costs O(N)O(N) space.

"""


import heapq


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
