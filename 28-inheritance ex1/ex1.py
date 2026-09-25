class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")


class Car(Vehicle):
    def accelerate(self):
        print("Car is accelerating")

v=Vehicle()
v.start()
v.stop()
print("------------------")
c=Car()
c.start()
c.stop()
c.accelerate()