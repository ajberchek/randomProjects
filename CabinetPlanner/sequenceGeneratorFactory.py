from sequenceGenerator import sequenceGenerator
from fibonacciGenerator import fibonacciGenerator

class sequenceGeneratorFactory:
    def __init__(self, numElems):
        self.numElems = numElems

    def createSequenceGenerator(self,sequenceType):
        if(sequenceType == "FIBONACCI"):
            return fibonacciGenerator(self.numElems)