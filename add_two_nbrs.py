# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:54:59 2020

@author: Home
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
        
    def link_list(self, new_val):
        new_node = ListNode(new_val)
        new_node.next = self.head
        self.head = new_node
    
    def addTwoNumbers(self, l1, l2):
        