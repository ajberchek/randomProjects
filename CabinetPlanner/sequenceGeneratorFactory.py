from fibonacciGenerator import fibonacciGenerator
from primeGenerator import primeGenerator

class sequenceGeneratorFactory:
    def __init__(self, numElems):
        self.numElems = numElems

    def createSequenceGenerator(self,sequenceType):
        if(sequenceType == "FIBONACCI"):
            return fibonacciGenerator(self.numElems)
        elif(sequenceType == "PRIME"):
            return primeGenerator(self.numElems)