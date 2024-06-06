class Calculator:

    def sum(self, a, b):
        result = a + b
        return result
    
    def sub(self, a, b):
        result = a - b
        return result
    
    def mul(self, a, b):
        result = a * b
        return result
    
    def div(self, a, b):
        if (b == 0):
            raise ArithmeticError("на ноль делить нельзя")
        else: 
            result = a / b
            return result
    
    def pow(self, a, b = 2):
        result = a ** b
        return result
    
    def avg(self, numbers):
        if(len(numbers) == 0):
            return 0
        s =0
        for num in numbers:
            s = self.sum(s, num)
        
        lenght = len(numbers)

        return self.div(s, lenght)



