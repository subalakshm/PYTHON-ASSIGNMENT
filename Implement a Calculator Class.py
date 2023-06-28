class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        Addition1 = self.num1+self.num2
        print("Addition of Num1 & Num 2:",Addition1)
    def subtract(self):
        Subtraction1 = self.num1-self.num2
        print("Subtraction of Num1 & Num 2:",Subtraction1)
    def multiply(self):
        Multipy1= self.num1*self.num2
        print("Multiply of Num1 & Num 2:",Multipy1)
    def divide(self):
        Divide1 = self.num1/self.num2
        print("Divide1 of Num1 & Num 2:",Divide1)
obj = Calculator(94, 10)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()