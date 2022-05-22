#https://www.youtube.com/watch?v=Dx2SE4hYy4g&list=PLRDzFCPr95fIgPrFFW-0nXT5YH6ZnjRM6&index=1

class TestClass:
    def instancemethod(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

a = TestClass()
print(a.staticmethod)