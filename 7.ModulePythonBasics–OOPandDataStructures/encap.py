class TestSome:
    def __init__(self,var1,var2):
        self.Var1 = var1
        self.Var2 = var2
    
    def testFunction(self):
        print("Hello I am Function")

object1 = TestSome("Apple","Banana")

print(object1.Var1)
object1.Var1 = "Orange"

print(object1.Var1)
object1.testFunction()

class TestSome1:
    def __init__(self,var1,var2):
        self.__Var1 = var1
        self.__Var2 = var2

    def getVar1(self): #getter
        return self.__Var1
    
    def changeVar1(self,input): #setter
        self.__Var1 = input

    def __testFunction(self):
        print("Hello I am Function")
    
    def runTestFunction(self):
        self.__testFunction()


object2 = TestSome1("Bike", "Car")
object2.runTestFunction()
print(object2.getVar1())
object2.changeVar1("Plan")
print(object2.getVar1())

class Test3:
    def __init__(self, var1):
        self._Var1 = var1

class ClidTest(Test3):
    def getVar(self):
        return self._Var1
    def changeVar1(self,input):
        self._Var1 = input







