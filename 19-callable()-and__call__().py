# Assingment-19

# Create a class Multiplier with an __init__() to set a factor.
#  Define a __call__() method that multiplies an input by the factor.
#  Test it with callable() and by calling the object like a function.


class Multipiller:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
m = Multipiller(5)

print(callable(m))
print(m(10))
        
        

