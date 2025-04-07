from queue import Queue


class MyStack:

    def __init__(self):
        self.data = Queue()

    def push(self, x: int) -> None:
        self.data.put(x)

    def pop(self) -> int:
        element = None
        tmp = Queue()
        while True:
            element = self.data.get()
            if self.empty():
                break
            tmp.put(element)

        while not tmp.empty():
            self.data.put(tmp.get())

        return element

    def top(self) -> int:
        tmp = self.pop()
        self.push(tmp)
        return tmp

    def empty(self) -> bool:
        return self.data.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()