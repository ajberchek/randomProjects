from sequenceGenerator import sequenceGenerator
class fibonacciGenerator(sequenceGenerator):
    def __init__(self,numElems):
        sequenceGenerator.__init__(self,numElems)
        self.fibSequence = []

    def getSequence(self):
        if(len(self.fibSequence) != 0):
            return self.fibSequence

        self.fibSequence.extend((0,1))
        for i in range(len(self.fibSequence),self.numElems):
            self.fibSequence.append(self.fibSequence[i-2]+self.fibSequence[i-1])

        return self.fibSequence