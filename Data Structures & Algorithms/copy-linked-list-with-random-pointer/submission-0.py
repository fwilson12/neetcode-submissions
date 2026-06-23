"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummy = Node(0)
        curr = dummy
        nodeDict = {} # O.G. Node memory add: Fresh memory add lol 

        while head:
            # instantiate curr if its equivalent doesn't exist already
            if head not in nodeDict:
                curr.next = Node(0)
                nodeDict[head] = curr.next # add {real: copy} object reference pair to dict
            # fetch curr if its already has been instantiated
            else:
                curr.next = nodeDict[head]
            # make curr current, and ready to be assigned values and next/random pointers
            curr = curr.next
            curr.val = head.val 
            
            # if the next node has already been instantiated, link curr to it
            if head.next in nodeDict:
                curr.next = nodeDict[head.next]
            
            # head.next is new to us, instantiate a node for it, fully construct it later
            else:
                # this is the last node in the list, don't add null to nodeDict
                if head.next is None:
                    curr.next = None
                # not the last, instantiate a node for it to be fully constructeed later
                else:
                    curr.next = Node(0)
                    nodeDict[head.next] = curr.next
            
            # same idea as above
            if head.random in nodeDict:
                curr.random = nodeDict[head.random]
            # same idea as above
            else:
                if head.random is None:
                    curr.random = None
                else:
                    curr.random = Node(0)
                    nodeDict[head.random] = curr.random
        
            head = head.next

            
        return dummy.next





