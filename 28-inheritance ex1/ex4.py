class Vehicle:

    def __init__(self):
        print("Vehicle created...")
    


class Car(Vehicle):
   def __init__(self): 
           print("Car created...")           
           super().__init__()


c=Car()
