# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        values = []                        # to stores the values that needed to be reverse

        nodes = []                         # to keep track of the nodes which needs to be reverse

        counter = 0

        curr = head

        while curr:

            counter += 1

            if counter >= left and counter <= right:

                values.append(curr.val)     #  | adding value and nodes in the list

                nodes.append(curr)          #  |

            curr = curr.next

        for node in nodes:

            node.val = values.pop(-1)       #  replace the value of nodes

        return head