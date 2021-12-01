from neurons import Neurons

class Perceptron:
    def __init__(self) -> None:
        self.neurons = [
            Neurons(['red','#ff0000']),
            Neurons(['green','#00ff00']),
            Neurons(['blue','#0000ff']),
            Neurons(['black','#000000']),
            Neurons(['white','#ffffff']),
            Neurons(['yellow','#ffff00']),
            Neurons(['magenta','#ff00ff']),
            Neurons(['cyan','#00ffff'])
        ]
        self.inputs = [
            [1.0, -1.0, -1.0], #red
            [-1.0, 1.0, -1.0], #green
            [-1.0, -1.0, 1.0], #blue
            [-1.0, -1.0, -1.0], #black
            [1.0, 1.0, 1.0], #white
            [1.0, 1.0, -1.0], #yellow
            [1.0, -1.0, 1.0], #magenta
            [-1.0, 1.0, 1.0] #cyan
        ]
        self.outputs  = [
            [1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], #red
            [-1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0], #green
            [-1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0, -1.0], #blue
            [-1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0, -1.0], #black
            [-1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0, -1.0], #white
            [-1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0, -1.0], #yellow
            [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0], #magenta
            [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0]  #cyan
        ]


    def training(self):
        cont = 0
        while cont < 100:
        
            for i in range(len(self.inputs)):
                for neuron in range(len(self.outputs)):
                    self.neurons[neuron].set_input(self.inputs[i])
                    self.neurons[neuron].linear()
                    self.neurons[neuron].adjust(self.outputs[i][neuron])
        
            cont+=1
    
    def result(self,color):
        result = []
        for i in range(len(self.neurons)):
            self.neurons[i].set_input(color)
            self.neurons[i].linear()
            result.append(self.neurons[i].get_output())
        
        return self.neurons[result.index(max(result))].name

    
    def minimax(self,x):
        x /= 255
        return (x * 2) - 1 

    def normalizar(self,color):
        for i in range(len(color)):
            color[i] = self.minimax(color[i])

    









