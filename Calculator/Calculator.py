class Calculator:
    def add(self, a, b):
        self.result = int(a) + int(b)
        return self.result

    def subtract(self, a, b):
        self.result = int(a) - int(b)
        return self.result

    def multiply(self, a, b):
        self.result = int(a) * int(b)
        return self.result

    def divide(self, a, b):
        self.result = round(int(a) / int(b), 9)
        return self.result

    def square(self, a):
        self.result = int(a) * int(a)
        return self.result

    def square_root(self, a):
        self.result = round(int(a) ** 0.5, 7)
        return self.result
