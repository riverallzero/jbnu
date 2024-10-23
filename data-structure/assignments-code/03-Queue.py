class Queue:

    def __init__(self): # 생성자
        self.array: list = []
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        self.rear += 1
        self.array.append(item)


    def dequeue(self):
        if self.isEmpty():
            print('Queue underflow')

        dequeue_val = self.array[self.front]
        self.front += 1

        return dequeue_val
    

    def peak(self):
        if self.isEmpty():
            print('Queue underflow')

        return self.array[self.front]
    
    
    def printElements(self):
        print(' '.join([str(val) for val in self.array]))


    def isEmpty(self):
        if self.size() == 0:
            return True
        
        return False


    def size(self):
        return self.rear - self.front + 1


if __name__ == '__main__':

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.printElements()       # 1 2 3 4 5

    print(queue.isEmpty())      # False

    print(queue.peak())         # 1
    print(queue.dequeue())      # 1
    print(queue.dequeue())      # 2
    print(queue.dequeue())      # 3
    print(queue.peak())         # 4
    print(queue.dequeue())      # 4
    print(queue.dequeue())      # 5
    print(queue.isEmpty())      # True
