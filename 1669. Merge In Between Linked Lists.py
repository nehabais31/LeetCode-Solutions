# -*- coding: utf-8 -*-
"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, 
and put list2 in their place.
uild the result list and return its head 
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
               
        start, end = None, list1
        for i in range(b):
            if i == a-1:
                start = end
            end = end.next
        start.next = list2    
        
        while list2.next :
            list2 = list2.next
        
        list2.next = end.next
        end.next = None
               
        return list1        
                
            
        