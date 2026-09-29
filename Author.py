class Author:
    def __init__(self, fname, lname, mname, dob):
        self._Fname = fname
        self._Lname = lname
        self._Mname = mname
        self._DOB = dob

#encasuplating the variables
    def getFname(self): return self._Fname
    def setFname(self, fname): self._Fname = fname
    def getLname(self): return self._Lname
    def setLname(self,lname): self._Lname = lname
    def getMname(self): return self._Mname
    def setMname(self, mname): self._Mname = mname
    def getDOB(self): return self._DOB
    def setDOB(self, dob): self._DOB = dob
    def getAge(self):
        return f'{self._DOB}'
    def getName(self):
        return f'{self._Fname} {self._Lname} {self._Mname}'




