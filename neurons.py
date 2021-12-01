import random

class Neurons:
    
    def __init__(self, name) -> None:
        self.weights = [random.randint(-100,100)/100 for i in range(3)] 
        self.input = [0] * 3
        self.output = 0
        self.learning = 0.01
        self.name = name

    def set_input(self,input):
        for i in range(len(input)):
            self.input[i] = input[i]

    def linear(self):
        aux= 1
        for x,w in zip(self.input,self.weights):
            aux += x * w
        self.output = aux   
    
    def get_output(self):
        return self.output
    
    def adjust(self,output):
        erro = output - self.output
        for i in range(len(self.input)):
            self.weights[i] = self.weights[i] + (self.learning * erro * self.input[i])
    


