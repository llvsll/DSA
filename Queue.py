class Queue:

    def __init__(self):
        self.Queue = []

    def enqueue(self, element):
        self.Queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.Queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.Queue[0]

    def isEmpty(self):
        return len(self.Queue) == 0

    def size(self):
        return len(self.Queue)


myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")

print("Queue: ", myQueue.Queue)
print("Pop: ", myQueue.dequeue())
print("Queue after Pop: ", myQueue.Queue)
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

myQueue.enqueue("D")

print("Queue after append: ", myQueue.Queue)
