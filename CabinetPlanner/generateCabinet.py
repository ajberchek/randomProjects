from CabinetConstraints import CabinetConstraints
from sequenceGeneratorFactory import sequenceGeneratorFactory
class GenerateCabinet:
    def __init__(self, width, height, rowHeight, numShelvesPerRow, sequenceType):
        self.cabinet = CabinetConstraints(width,height,rowHeight,numShelvesPerRow)
        self.sequenceFactory = sequenceGeneratorFactory(self.cabinet.getRequiredSequenceSize())
        self.sequenceGenerator = self.sequenceFactory.createSequenceGenerator(sequenceType)

    def generateCabinetLayout(self):
        self.cabinet.clearLayout()
        self.cabinet.layoutShelves(self.sequenceGenerator.getSequence())
        print(self.cabinet)

GCab = GenerateCabinet(17,20,2,5,"FIBONACCI")
GCab.generateCabinetLayout()