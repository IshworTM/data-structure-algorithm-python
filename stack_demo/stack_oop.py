class Stack:
    def __init__(self, max_size: int):
        self.max_size = self.validate_max_size(max_size)
        self.stack = [None] * self.max_size
        self.top = -1

    def validate_max_size(self, max_size: int) -> int | ValueError:
        if max_size >= 0:
            return max_size
        raise ValueError("Max-size must be a positive integer.")

    def push(self, value: int) -> int:
        if self.is_full():
            return None
        self.top += 1
        self.stack[self.top] = value
        return value

    def pop(self) -> int:
        if self.is_empty():
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def is_full(self) -> bool:
        return self.top == self.max_size - 1

    def is_empty(self) -> bool:
        return self.top == -1

    def peek(self) -> int:
        if self.is_empty():
            return None
        return self.stack[self.top]

    def display(self) -> list:
        res = []
        for idx, el in enumerate(self.stack):
            label = ""
            if idx == self.top:
                label = "(T)"
            res.append(f"{label}{el}")
        return res


if __name__ == "__main__":
    stack = Stack(5)
    print(stack.is_empty())
    print(f"Pushed: {stack.push(10)}")
    print(f"Display: {stack.display()}")
    print(f"Pushed: {stack.push(30)}")
    print(f"Display: {stack.display()}")
    print(f"Pushed: {stack.push(20)}")
    print(f"Display: {stack.display()}")
    print(f"Pushed: {stack.push(432)}")
    print(f"Display: {stack.display()}")
    print(f"Pushed: {stack.push(1234)}")
    print(f"Display: {stack.display()}")
    print(f"Popped: {stack.pop()}")
    print(f"Display: {stack.display()}")
    print(f"Pushed: {stack.push(891)}")
    print(f"Display: {stack.display()}")
    print(stack.is_full())
