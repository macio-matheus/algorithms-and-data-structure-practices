"""
Você recebe duas listas vinculadas não vazias que representam dois números inteiros não negativos. Os dígitos são
armazenados na ordem inversa e cada um de seus nós contém um único dígito. Adicione os dois números e
retorne-o como uma lista vinculada.

Você pode assumir que os dois números não contêm nenhum zero inicial, exceto o próprio número 0.

Exemplo:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explain: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            carry, out = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next
