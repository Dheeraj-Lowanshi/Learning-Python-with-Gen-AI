class Vehicle:

    def __init__(self):
        print("Vehicle created...")
    


class Car(Vehicle):
   def __init__(self):           
           super().__init__()
           print("Car created...")


c=Car()
