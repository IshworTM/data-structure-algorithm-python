class LinearQueue:
    def __init__(self, max_size: int):
        self.max_size = self.validate_max_size(max_size)
        self.queue = [None] * self.max_size
        self.front = -1
        self.rear = -1

    def validate_max_size(self, max_size):
        if max_size >= 0:
            return max_size
        raise ValueError("Max-size must be a positive integer.")

    def enqueue(self, item) -> list | None:
        if self.is_full():
            return None
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        return item

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return item

    def display(self) -> list:
        queue = []
        for idx, val in enumerate(self.queue):
            label = ""
            if idx == self.front and idx == self.rear:
                label = "(F,R)"
            elif idx == self.front:
                label = "(F)"
            elif idx == self.rear:
                label = "(R)"
            queue.append(f"{label}{val}")
        return queue

    def is_empty(self) -> bool:
        return self.front == -1

    def is_full(self) -> bool:
        return self.rear == self.max_size - 1


if __name__ == "__main__":
    lqueue = LinearQueue(5)
    print(lqueue.is_empty())
    print(lqueue.display())
    print(f"Enqueued: {lqueue.enqueue(10)}")
    print(lqueue.display())
    print(f"Enqueued: {lqueue.enqueue(30)}")
    print(lqueue.display())
    print(f"Enqueued: {lqueue.enqueue(20)}")
    print(lqueue.display())
    print(f"Enqueued: {lqueue.enqueue(432)}")
    print(lqueue.display())
    print(f"Enqueued: {lqueue.enqueue(1234)}")
    print(lqueue.display())
    print(f"Dequeued: {lqueue.dequeue()}")
    print(lqueue.display())
    print(f"Enqueued: {lqueue.enqueue(891)}")
    print(lqueue.display())
    print(lqueue.is_full())
