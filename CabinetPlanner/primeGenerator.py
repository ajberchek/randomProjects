from sequenceGenerator import sequenceGenerator
import math

class primeGenerator(sequenceGenerator):
    def __init__(self,numElems):
        sequenceGenerator.__init__(self,numElems)
        self.primeSequence = []

    def getSequence(self):
        if(len(self.primeSequence) != 0):
            return self.primeSequence

        currentNumberCheck = 2
        while(len(self.primeSequence) < self.numElems):
            currentNumberPrime = True
            for i in range(2,int(math.sqrt(currentNumberCheck))+1):
                if(currentNumberCheck % i == 0):
                    currentNumberPrime = False

            if(currentNumberPrime):
                self.primeSequence.append(currentNumberCheck)

            currentNumberCheck += 1

        return self.primeSequence


