class Parent():
    def __init__(self,last_name,eye_color):
        print "Parent constructer called"
        self.last_name=last_name
        self.eye_color=eye_color
        
class Child(Parent):
    def __init__(self,last_name,eye_color,no_of_toys):
        print "child constructer called"
        Parent.__init__(self,last_name,eye_color)
        self.no_of_toys=no_of_toys
    
billy_cyrus=Parent("Cyrus","blue")

print billy_cyrus.last_name

miley_cyrus=Child("Cyrus","blue",5)
print miley_cyrus.last_name
print miley_cyrus.no_of_toys
