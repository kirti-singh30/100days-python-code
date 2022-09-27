def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
       
print(add(2,4,5,6,7))


def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3,add= 4, multiply= 6 )

class Car:
    # def __init__(self,**kwargs):
    #     self.make = kwargs["make"]
    #     self.model = kwargs["model"]

    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
my_car = Car( model = "X-5",make = "BMW")
print(my_car.model)
print(my_car.make)