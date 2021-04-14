class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        newNode = Node(data)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = newNode

    def removeLoop(self):
        cur = self.head
        cur2 = self.head
        while (cur and cur2 and cur2.next):
            cur = cur.next
            cur2 = cur2.next.next
            print(cur.data)
            print(cur2.data)
            if cur == cur2:
                break
        loopNode = cur
        cur = self.head
        cur2 = loopNode
        while 1:
            cur2 = loopNode
            while cur2.next != loopNode:
                if cur2.next == cur:
                    cur2.next = None
                    return
                cur2 = cur2.next
            cur = cur.next
        return


    def display(self):
        curr = self.head
        while curr.next!=None:
            curr = curr.next
            print('data at node is %s' % curr.data)


if __name__ == '__main__':
    l = LinkedList()
    l.insert(3)
    l.insert(7)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.insert(8)
    #print(l.head.next.next.next.next.next.data)
    l.head.next.next.next.next.next.next = l.head.next.next
    #l.display()
    l.removeLoop()
    l.display()