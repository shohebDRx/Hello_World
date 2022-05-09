
class A:
    def Feature1(self):
        print("Feature 1 is working")
    def Feature2(self):
        print("Feature 2 is working")
        
class B:
    def Feature3(self):
        print("Feature 3 is Working")
    def Feature4(self):
        print("Feature 4 is working")

def C(A,B):
    def Feature5(self):
        print("Feature 5 is working")

c1=C()
c1.Feature5()
