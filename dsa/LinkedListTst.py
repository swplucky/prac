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

    def display(self):
        curr = self.head
        while curr.next!=None:
            curr = curr.next
            print('data at node is %s' % curr.data)


if __name__ == '__main__':
    l = LinkedList()
    l.insert(3)
    l.display()