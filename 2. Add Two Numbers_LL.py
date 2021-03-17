# -*- coding: utf-8 -*-
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

"""

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, newNode):
        if self.head is None:
            self.head = newNode
        else:     
            lastNode = self.head 
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
        
    def print_ll(self):
        curr_node = self.head 
        if curr_node is None:
            return
        
        while curr_node is not None:
            print(curr_node.val)
            curr_node = curr_node.next
            
class Solution:
    def addTwoNumbers(self, l1, l2) :
        dummy = res =  ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry +=  l1.val
                l1 = l1.next
            if l2:
                carry +=  l2.val
                l2 = l2.next
            
            carry, val = divmod(carry, 10)
            dummy.next = ListNode(val)
            dummy = dummy.next
        #return res.next 
        
        node = res.next
        while node:
            print(node.val)
            node = node.next
 
        
list1 = LinkedList()

firstNode = ListNode(2)
secondNode = ListNode(4) 
thirdNode = ListNode(3)

list1.insert_node(firstNode)
list1.insert_node(secondNode)
list1.insert_node(thirdNode)


list2 = LinkedList()

firstNode2 = ListNode(5)
secondNode2 = ListNode(6) 
thirdNode2 = ListNode(4)
 
      
list2.insert_node(firstNode2)
list2.insert_node(secondNode2)
list2.insert_node(thirdNode2)

# Add numbers of 2 link list
sol = Solution()
list3 = sol.addTwoNumbers(list1.head, list2.head)


