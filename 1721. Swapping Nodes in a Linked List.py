# -*- coding: utf-8 -*-
"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after 
swapping the values of the kth node from the beginning 
and the kth node from the end (the list is 1-indexed).
"""

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        
    def add_elements(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node
    
    
    def print_list(self):
        print_val = self.head
        while print_val:     # not NOne
           print(print_val.data, end = ' ')
           print_val = print_val.next
           
           
class Solution:
    def swapNodes(self, head, k): 
        slow = fast = head
        
        # For getting the kth node from beginning
        for i in range(k-1):
            fast = fast.next 
        first = fast 
        
        while fast.next:
            fast = fast.next 
            slow = slow.next  
        
        # At end of loop slow is pointing to kth node from end
        # Swap their data
        slow.data, first.data = first.data , slow.data 
        
        return head     
        

ll = Linked_List()


ll.add_elements(1)
ll.add_elements(2)
ll.add_elements(3)
ll.add_elements(4)
ll.add_elements(5)  

sol = Solution()
sol.swapNodes(ll.head, 2)

ll.print_list()
            