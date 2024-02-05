class Safoorji:
    #parameter based data for the function.
    def __init__(self,Block_No,Room_No):
        self.Block_No=Block_No
        self.Room_No=Room_No
    def show(self,done):
        print("Enjoying the building no:{} and the room:{} python writing:".format(self.Block_No,self.Room_No),done)
    #no-parameterised data for the function.
    def run(self):
        return 34
obj=Safoorji("L64",506)
#Accessing class method.
obj.show(50.56)
print(obj.run())

#Creating an Empty Class in Python.
class Dear:
    pass

#Inheritance in python
class Run:
    def __init__(self):
        print("Initial Constructor")
    def action(self,motion):
        motion=2*motion
class Play(Run):
    def decision(self,action):
        action=action*2
    def action(motion):
        motion=motion**3
objRun=Run()
objRun.action(30)
objRun1=Play
print(objRun1.action(23))
print(objRun1.decision(objRun1,45))

#Abstraction in python
from abc import ABC, abstractmethod 

class democlass(ABC): 
   @abstractmethod 
   def method1(self): 
    print ("abstract method") 
    return 

   def method2(self): 
    print ("concrete method") 

class concreteclass(democlass): 
    def method1(self): 
        super().method1() 
        return 

obj = concreteclass() 
obj.method1()  #abstract method 
obj.method2()  #concrete method 

#Abstraction practice
#Note:SubClass has its method which inherit abstract class. These subClass must inherit all the methods of abstract class which contains @abstractMethod keyword.
from abc import ABC, abstractmethod 

class democlass(ABC):
   @abstractmethod
   def methodChk(self):
    pass  

   @abstractmethod 
   def method1(self): 

      print ("abstract method") 

      return 

   def method2(self): 
    print ("concrete method") 

class concreteclass(democlass): 

    def method1(self): 

       super().method1() 

       return 
    def methodChk(self):
       print("ddd fff")
class concreteClassVal(democlass): 

      def method1(self): 

           super().method1() 

           return 

      def methodChk(self):
         print("It is used to perform action") 
      def action(self,grass):
         print("all input",grass)

obj = concreteclass() 
val=obj.method1()  #abstract method 
print(val)
obj.method2()  #concrete method 
print("-------------------")
obj1=concreteClassVal()
valObj1=obj1.method1()
obj1.methodChk()
obj1.method2()
obj1.action("hh YYY")
