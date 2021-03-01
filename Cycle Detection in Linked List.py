# -*- coding: utf-8 -*-
"""
To find if there is any cycle in Linked List

Floyd's Cycle Detecting Algorithm
1. Initialize 2 pointers (slow, fast) initially at head.
2. Traverse the list
3. Move the slow pointer one step forward and the fast pointer two steps forward
4. If there’s a loop, at some point, the fast pointer will meet
   the slow pointer and overtake it.
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
        while print_val:     # not NOne
           print(print_val.data, end = ' ')
           print_val = print_val.next_val
           
           
class Solution:
    def finding_cycle(self, head):
        slow = fast = head
        while (slow and fast and fast.next_val):
            slow = slow.next_val
            fast = fast.next_val.next_val 
            if slow == fast:
                return True
        return False
    

ll = Linked_List()


ll.add_elements(1)
ll.add_elements(2)
ll.add_elements(3)
ll.add_elements(4)
ll.add_elements(5)     


# Lets create a loop for testing purpose
ll.head.next_val.next_val.next_val = ll.head

res = Solution()

if (res.finding_cycle(ll.head)) :
    print('Has Cycle')
else:
    print('No Cycle')    
