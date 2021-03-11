# -*- coding: utf-8 -*-
"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""


class ListNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        
    def add_elements(self, new_data):
        new_node = ListNode(new_data)
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
    def getDecimalValue(self, head):
        if not head:
            return
        
        listValues = ''
        
        while head:
            listValues += str(head.data)
            head = head.next

        return int(listValues, 2)            
    

ll = Linked_List()


ll.add_elements(1)
ll.add_elements(1)
ll.add_elements(1)


sol = Solution()
print(sol.getDecimalValue(ll.head))

