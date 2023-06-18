# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow,fast=head,head
    while fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
