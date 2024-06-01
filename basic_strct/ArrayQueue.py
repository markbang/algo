class ArrayQueue:
    

    def __init__(self):
        self._queue=[]

    def __len__(self):
        return len(self._queue)
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def enqueue(self, e):
        return self._queue.append(e)
    
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._queue[0]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._queue.pop(0)
    
class Empty(Exception):
    """Error attempting to access an element from an empty container."""

if __name__=="__main__":
    queue = ArrayQueue()
    print(queue.first())
    queue.enqueue(10)
    queue.enqueue(5)
    print(queue.__len__())
    print(queue.is_empty())
    print(queue.first())
    print(queue.dequeue())
    print(queue.first())