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

    
