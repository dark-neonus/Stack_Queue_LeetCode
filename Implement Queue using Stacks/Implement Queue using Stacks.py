from queue import LifoQueue

Stack = LifoQueue

class MyQueue:
    def __init__(self):
        self.data : Stack = Stack()

    def push(self, x: int) -> None:
        tmp = Stack()

        while not self.data.empty():
            tmp.put(self.data.get())

        self.data.put(x)

        while not tmp.empty():
            self.data.put(tmp.get())


    def pop(self) -> int:
        return self.data.get()

    def peek(self) -> int:
        tmp = self.data.get()
        self.data.put(tmp)
        return tmp

    def empty(self) -> bool:
        return self.data.empty()

    def copy_stack(self) -> Stack:
        result = Stack()
        tmp = Stack()

        while not self.data.empty():
            item = self.data.get()
            result.put(item)
            tmp.put(item)

        while not tmp.empty():
            self.data.put(tmp.get())

        return result
