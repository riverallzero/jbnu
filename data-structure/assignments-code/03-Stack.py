# Stack class 구현

class Stack:
    def __init__(self): # 생성자
        self.array: list = []
        self.top = -1


    def push(self, item: int) -> None:  # null / nullptr
        self.top += 1
        self.array.append(item)


    def pop(self) -> int:
        if self.isEmpty():
            print('Stack underflow')

        pop_val = self.array[self.top]
        self.top -= 1

        return pop_val


    def peak(self) -> int:
        if self.isEmpty():
            print('Stack underflow')

        return self.array[self.top]


    def printElements(self) -> None:
        print(' '.join([str(val) for val in self.array])) 


    def isEmpty(self) -> bool:
        if self.size() == 0:
            return True
        
        return False
    

    def size(self):
        return self.top + 1


if __name__ == '__main__':

    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.printElements()       # 1 2 3 4 5

    print(stack.isEmpty())      # False

    print(stack.peak())         # 5
    print(stack.pop())          # 5
    print(stack.pop())          # 4
    print(stack.pop())          # 3
    print(stack.peak())         # 2
    print(stack.pop())          # 2
    print(stack.pop())          # 1

    print(stack.isEmpty())      # True
