class MyQueue:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        x = self.q[0]
        self.q.pop(0)
        return x
        

    def peek(self) -> int:
        x = self.q[0]
        return x
        

    def empty(self) -> bool:
        if self.q == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()