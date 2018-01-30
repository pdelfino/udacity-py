
class Parent:

    def __init__(self, last_name, eye_color):
        
        print ("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):

        print ("Last name: "+self.last_name, "Eye color: "+self.eye_color)

example = Parent('Delfino', "black")

# print (example.last_name, example.eye_color) # ok

class Child(Parent):

    def __init__(self, last_name, eye_color, number_of_toys):

        print ("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        

miley_cirus = Child("Cirus", "Blue", 5)

# print (miley_cirus.last_name, miley_cirus.number_of_toys)

example.show_info()

# miley_cirus uses Child, which inherits Parent. So, it inherits the method

miley_cirus.show_info()
