'''
class Myclass:
    """Greetings try"""
    l=12345
    def f(self):
        return("hello world")



print(Myclass.l)
print(Myclass.__doc__)
print(Myclass.f)
print(Myclass())
abc=Myclass()
print(abc.f())

'''
class student:
    '''Student class'''
    def __init__(self,n,a):
        self.full_name=n
        self.age=a
    def get_age(self):
        #return self.age+2
        print(self.age+2)

"""
print(student.__doc__)
f=student('Bobby boy',23)#instance is created
print(f.age)
f.age=32
print(f.age)
#print(f.get_age())
f.get_age()

print(getattr(f,"full_name"))"""

class cs_class(student):
    def __init__(self, n, a,s):
        #super().__init__(n, a) 3
        student.__init__(self,n,a)
        self.section_num=s
        
    def get_age(self): # get_age():#needs 'self' as a parameter, since it is a class method and not a function. Adding that should make it work fine.
        #return super().get_age()
        #print(super().get_age())
        print("Age: "+ str(self.age))

f=cs_class("VISH",25,13)
f.get_age()
print(dir(f))