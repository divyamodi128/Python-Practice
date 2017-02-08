def fib(n):
    """Display the n first terms of Fibonacci sequence"""
    a, b = 0, 1
    i = 0
    while i < n:
        print(b)
        a, b = b, a + b
        i += 1


class FibonacciSeq():
    def __init__(self):
        self.a, self.b = 0, 1

    def printFibo(self, n):
        if n > 0:
            print(self.a)
            self.a, self.b = self.b, self.a + self.b
            self.printFibo(n - 1)

fibo = FibonacciSeq()
fibo.printFibo(10)
if __name__ == '__main__':
    fib(10)

