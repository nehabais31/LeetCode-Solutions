# -*- coding: utf-8 -*-
"""
Create a linked list 
Traverse through the linked list
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_val = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        val = self.head
        while val is not None:
            print(val.data, end = ' ')
            val = val.next_val
        
list1 = Linked_List()
list1.head = Node(1)
element2 = Node(2)
element3 = Node(3)

# Assign links from nodes
list1.head.next_val = element2
element2.next_val = element3     

list1.print_list()  
        