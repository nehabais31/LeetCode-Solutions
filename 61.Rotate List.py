# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:      
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        lastElement = head
        length = 1
        while lastElement.next :
            lastElement = lastElement.next
            length += 1
            
        # if k = length of list then k % length = 0
        # elif k > length then k = k % length
        k = k % length
        
        # Create a circular list by pointing the lastElement.next to head
        lastElement.next = head
        
        # Traverse the list just before the lastElement - k node
        # If list = 1 -> 2 -> 3 -> 4 -> 5 and k = 3
        # Traverse till 5 - 3 -1 = 2nd node 
        # set this second node next to None
        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next
        
        result = tempNode.next 
        tempNode.next = None
        
        
        return result
        
        
        

head = [1, 2, 3, 4, 5]




# =============================================================================
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None                
# 
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         
#     def insertNode(self, newNode):
#         if self.head is None:
#             self.head = newNode
#         else:
#             currNode = self.head 
#             while currNode.next is not None:
#                 currNode = currNode.next
#             currNode.next = newNode
#             
#     def rotateList(self, k):
#         if self.head is None or k == 0:
#             return 
#         
#         currNode = prevNode = self.head 
#         while k > 0:
#             while currNode.next is not None:
#                 prevNode = currNode
#                 currNode = currNode.next
#                 
#             currNode.next = self.head  
#             prevNode.next = None
#             self.head = currNode
#             k -= 1
#         
#             
#     def printLinkList(self):
#         if self.head is None:
#             return
#         else:
#             currNode = self.head
#             while currNode is not None:
#                 print(currNode.data)
#                 currNode = currNode.next 
#                 
# ll = LinkedList()
# 
# ll.insertNode(Node(0))
# ll.insertNode(Node(1))
# ll.insertNode(Node(2))
# ll.insertNode(Node(4))
# ll.insertNode(Node(5)) 
# 
# ll.printLinkList()  
# 
# #ll.rotateList(1)
# 
# print('\nList after 1st rotation')
# ll.printLinkList()
# 
# ll.rotateList(2)
# 
# print('\nList after 2nd rotation')
# ll.printLinkList()
# =============================================================================
