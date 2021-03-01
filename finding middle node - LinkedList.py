'''
1. Initilaize 2 pointers fast and slow initially pointing to head.
2. Move slow by one step and fast by 2 steps till fast reaches end
3. Check for fast position, if None return slow pointer data element else,
   slow.data , slow.next.data

Odd #  of nodes |   Middle Node 
===============================
1				|     1
3				|	  2
5				|     3
7				|	  4
9				|     5

In every step, the number of nodes increases by two 
whereas the position of the middle node is increasing by one.

Even #of nodes  |   Middle Node 
===============================
2				|     1,2
4				|	  2,3
6				|     3,4
8				|	  4,5
10				|     5,6

In case of even, only diff is we have two middle nodes.
In order to find whether # of nodes is even or odd:
1. If even, after lasts iteration the fast node will point to tail node
   (since we are incrementing it by 2)
2. If odd, after last iteration, the fast node will point to None.

'''

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
    def finding_middle(self, head):
        slow = fast = head
        while (fast and fast.next) :
            slow = slow.next
            fast = fast.next.next 
        if not fast:
           return [slow.data, slow.next.data]
        else:
            return slow.data


ll = Linked_List()

ll.add_elements(1)           
ll.add_elements(3)    
ll.add_elements(5)    
ll.add_elements(7)    
ll.add_elements(9)    

ll.print_list()

sol = Solution()
middle_node = sol.finding_middle(ll.head)
print('\n', middle_node)