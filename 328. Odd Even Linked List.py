# -*- coding: utf-8 -*-
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Four conditions for the while-loop:

odd and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
odd and even.next -> wrong when 1->2->3->4->5->None ( odd nodes ) because even is None, which has no attribute 'next'
even and odd.next -> wrong when 1->2->3->4->None ( even nodes ) because even.next is None, which has no attribute 'next'
even and even.next -> correct
1. when 1->2->3->4->5->None ( odd nodes ) even will become None first and at the same time, odd points at the last node of the linked list; therefore, breaks from the while loop.
2. when 1->2->3->4->None ( even nodes ) even.next will become None first and at the same time, odd points at the last-2 node of the linked list and even points at the last node of the linked list; therefore, breaks from the while loop.


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
    def oddEvenList(self, head) :
        if not head:
            return head
               
        # Set odd and even pointers
        odd = head
        even = head.next
        evenHead = even
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
            
        odd.next = evenHead    
        return head   
    

ll = Linked_List()


ll.add_elements(1)
ll.add_elements(2)
ll.add_elements(3)
ll.add_elements(4)
ll.add_elements(5)     

ll.print_list()

sol = Solution()
sol.oddEvenList(ll.head)


print('\nOdd first and even next')
ll.print_list()


