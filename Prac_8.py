print("Archana Vyas 20CE157")

class Parent():
	
    def volume(self,l,b,h):
        self.vol = l*b*h
        print(self.vol)
        print("Inside Parent")
		
class Child(Parent):

    def volume(self,l,b,h):
        if(l==b and l==h):
            self.vol = l**3
            print(self.vol)
            print("Inside Child")
        else:
            super().volume(l,b,h)
		
# Driver's code
l=int(input("Enter l:"))
b=int(input("Enter b:"))
h=int(input("Enter h:"))

obj = Child()
obj.volume(l,b,h)


