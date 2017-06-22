import sys
class CabinetConstraints:
    def __init__(self, width, height, rowHeight, numShelvesPerRow):
        self.width = width
        self.height = height
        self.rowHeight = rowHeight
        self.numShelvesPerRow = numShelvesPerRow
        self.numRows = int(height/rowHeight)
        self.shelfLayout = [["_" for x in range(self.width)] for y in range(self.numRows)]

    def getRequiredSequenceSize(self):
        return self.numRows*self.numShelvesPerRow

    def clearLayout(self):
        self.shelfLayout = [["_" for x in range(self.width)] for y in range(self.numRows)]

    def layoutShelves(self,sequence):
        print(len(sequence))
        lastShelfPos = 0
        for i in range(self.numRows):
            for j in range(self.numShelvesPerRow):
                sequenceIndex = i*self.numShelvesPerRow + j

                lastShelfPos = (lastShelfPos + sequence[sequenceIndex]) % self.width
                self.shelfLayout[i][lastShelfPos] = "|"

    def __str__(self):
        toRet = " "
        for i in range(self.width):
            toRet += "_"
        toRet += " \n"
        for i in range(self.numRows-1,0,-1):
            toRet += "|"
            for j in range(self.width):
                toRet += self.shelfLayout[i][j]
            toRet += "|\n"
        return toRet

