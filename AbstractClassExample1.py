from abc import ABC,abstractmethod;

class Demo(ABC):
    @abstractmethod
    def test1(self):
        pass



class XYZ(Demo):
    def test1(self):
        print("Test Method")

d1=XYZ();
d1.test1();
