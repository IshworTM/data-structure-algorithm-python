from linear_queue import LinearQueue


class CircularQueue(LinearQueue):
    def __init__(self, max_size):
        super().__init__(max_size)

    def enqueue(self, item: int) -> int | None:
        if self.is_full():
            return None
        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.max_size
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
            self.front = (self.front + 1) % self.max_size
        return item

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front


if __name__ == "__main__":
    cqueue = CircularQueue(5)
    print(cqueue.display())
    print(cqueue.is_empty())
    print(cqueue.display())
    print(f"Enqueued: {cqueue.enqueue(10)}")
    print(cqueue.display())
    print(f"Enqueued: {cqueue.enqueue(30)}")
    print(cqueue.display())
    print(f"Enqueued: {cqueue.enqueue(20)}")
    print(cqueue.display())
    print(f"Enqueued: {cqueue.enqueue(432)}")
    print(cqueue.display())
    print(f"Enqueued: {cqueue.enqueue(1234)}")
    print(cqueue.display())
    print(f"Dequeued: {cqueue.dequeue()}")
    print(cqueue.display())
    print(f"Enqueued: {cqueue.enqueue(891)}")
    print(cqueue.display())
    print(cqueue.is_full())
