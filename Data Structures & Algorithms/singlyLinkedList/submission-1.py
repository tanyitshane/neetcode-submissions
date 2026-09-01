class ListNode:

    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(val = -1)
        self.tail = self.head

    def get(self, index: int) -> int:

        current = self.head.next
        counter = 0

        while current is not None:
            if counter == index: 
                return current.val

            counter += 1
            current = current.next
        
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        current = self.head.next
        prev = self.head
        counter = 0

        while current is not None:
    
            if counter == index:
                if current == self.tail:
                    self.tail = prev
                prev.next = current.next
                return True

            counter += 1
            prev = current
            current = current.next
        
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        arr = []
        while current is not None:
            arr.append(current.val)
            current = current.next

        return arr
        
