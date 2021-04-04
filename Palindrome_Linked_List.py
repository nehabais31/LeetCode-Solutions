# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:22:37 2021

@author: Home
"""


class ListNode():
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None

    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            currNode = self.head 
            while currNode.next :
                currNode = currNode.next
            currNode.next = newNode 

    def printLinkedList(self):
        currNode = self.head 
        while currNode :
            print(currNode.data)
            currNode = currNode.next 


class Solution():
    def isPalindrome(self, head):
        string = ''
        while head:
            string += str(head.data)
            head = head.next
        
        return string == string[::-1]


ll = LinkedList()

ll.insertNode(ListNode(1))
ll.insertNode(ListNode(2))
ll.insertNode(ListNode(2))
ll.insertNode(ListNode(1))

ll.printLinkedList()

sol = Solution()

print(sol.isPalindrome(ll.head))

              
            
    
    