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
        return new_node

    def addTwoNumbers(self, l1, l2):
        # Initialize carry and result 
        carry = 0
        result = ListNode(0)

        while l1 or l2:
            #calculate sum and store carry over value
            total = carry
            total += 0 if l1 is None else l1.val
            total += 0 if l2 is None else l2.val

            # Check if the addition is greater than 10
            # and compute carry over value
            if total >= 10:
                carry = 1
                total = total % 10
            else:
                carry = 0

            result.next =  ListNode(total)
            result = result.next

            # Base cases
            # if the 2 linked lists are not of same size
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

            return result.next

def print_list(l):
    if l is None:
        return ''
    return str(l.val) + ',' + print_list(l.next)   

# Driver Code
sol = Solution()
l1 = sol.link_list(2)
l1 = sol.link_list(4)
l1 = sol.link_list(3)
print(print_list(l1))

# Second linked list
l2 = sol.link_list(5)
l2 = sol.link_list(6)
l2 = sol.link_list(4)
print(print_list(l2))

# Adding two link list
s = Solution()
l3 = s.addTwoNumbers(l1, l2)
print(print_list(l3))




        