class Author:
    def __init__(self):
        self.fName = ''
        self.lName = ''
        self.publishingHouse = ''
        self.datePublished = 0

    def setName(self, fn: str, ln: str):
        self.fName = fn
        self.lName = ln

    def getName(self):
        return self.fName, self.lName

    def setPublishingHouse(self, ph: str):
        self.publishingHouse = ph

    def getPublshingHouse(self):
        return self.publishingHouse

    def setDatePublished(self, datetime):
        self.datePublised = datetime

    def getDataPublished(self):
        return self.datePublished




