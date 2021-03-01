# -*- coding: utf-8 -*-
"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together 
the nodes of the first two lists.
"""

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next_val = None

class Linked_List:
    def __init__(self):
        self.head = None
        
    def add_elements(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        tail = self.head
        while tail.next_val:
            tail = tail.next_val
        
        tail.next_val = new_node
    
    
    def print_list(self):
        print_val = self.head
        while print_val is not None:
           print(print_val.data, end = ' ')
           print_val = print_val.next_val
 
class Solution:
          
    def merge_lists(self, head_1, head_2):
        dummy = Node(0)
        tail = dummy
        
        while True:
            # Base cases 
            # if one of the list gets empty, return the other list
            if head_1 is None:
                tail.next_val = head_2
                break
            elif head_2 is None:
                tail.next_val = head_1
                break
                
            if head_1.data < head_2.data:
                tail.next_val = head_1
                head_1 = head_1.next_val
            else:
                tail.next_val = head_2
                head_2 = head_2.next_val
                
            tail = tail.next_val
        return dummy.next_val        
            
           

list1 = Linked_List()
list2 = Linked_List()

list1.add_elements(1) 
list1.add_elements(4)
list1.add_elements(8)
print('List 1: ', end = ' ')
list1.print_list()
print()

list2.add_elements(1)
list2.add_elements(2)
list2.add_elements(3)
list2.add_elements(5)
list2.add_elements(9)        
print('List 2: ', end = ' ')
list2.print_list()
print()

res = Solution()
list1.head = res.merge_lists(list1.head, list2.head)
print('Merged Lists: ', end = ' ')
list1.print_list()
print()
             
             


