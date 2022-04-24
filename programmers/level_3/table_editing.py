# 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81301

class LinkedList:
    class Node():
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next
            self.deleted = False

    def __init__(self, n, k):
        self.root = self.Node(0)
        self.current = self.root
        self.stack = []
        temp = self.root
        for i in range(1, n):
            new_node = self.Node(i, prev=temp)
            temp.next = new_node
            if i == k:
                self.current = new_node
            temp = new_node

    def up(self, count):
        for _ in range(count):
            self.current = self.current.prev

    def down(self, count):
        for _ in range(count):
            self.current = self.current.next

    def remove(self):
        nodeToDelete = self.current
        nodeToDelete.deleted = True
        self.stack.append(nodeToDelete)
        # root를 지울 경우
        if self.current == self.root:
            self.root = self.root.next
            self.root.prev = None
            self.current = self.root
        # 맨 끝을 지울 경우
        elif self.current.next is None:
            self.current = self.current.prev
            self.current.next = None
        # 가운데를 지울 경우
        else:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.next

    def revert(self):
        nodeToRevert = self.stack.pop()
        nodeToRevert.deleted = False
        # prev가 None인 node를 살릴 경우 맨 처음에 배치
        if nodeToRevert.prev is None:
            nodeToRevert.next.prev = nodeToRevert
            self.root = nodeToRevert
        # next가 None인 node를 살릴 경우 맨 마지막에 배치
        elif nodeToRevert.next is None:
            nodeToRevert.prev.next = nodeToRevert

        # 중간에 배치
        else:
            # 살릴 node보다 위에 있고 삭제되지 않은 node 중 가장 처음 보이는 node와 연결
            prevNode = nodeToRevert.prev
            while prevNode.deleted:
                prevNode = prevNode.prev
            nodeToRevert.prev = prevNode
            prevNode.next = nodeToRevert

            # 살릴 node보다 아래에 있고 삭제되지 않은 node 중 가장 처음 보이는 node와 연결
            nextNode = nodeToRevert.next
            while nextNode.deleted:
                nextNode = nextNode.next
            nextNode.prev = nodeToRevert
            nodeToRevert.next = nextNode

    def getRoot(self):
        return self.root


def solution(n, k, cmd):
    linkedlist = LinkedList(n, k)

    for c in cmd:
        if 'U' in c:
            linkedlist.up(int(c.split()[1]))
        elif 'D' in c:
            linkedlist.down(int(c.split()[1]))
        elif 'C' in c:
            linkedlist.remove()
        else:
            linkedlist.revert()
    answer = ['X']*n
    current = linkedlist.getRoot()
    while current:
        answer[current.value] = 'O'
        current = current.next
    return ''.join(answer)


cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
cmd = ["C", "C", "C", "C", "C", "Z", "Z", "Z", "Z", "Z"]
print(solution(6, 0, cmd))
