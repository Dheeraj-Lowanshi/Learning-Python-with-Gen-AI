class Math:
    def __init__(self):
        self.x=10
        self.y=20
        Math.z=30
              
    @staticmethod
    def add(a,b):
        sum=a+b
        print("Sum is",sum)
        print("z:",Math.z)

obj=Math()
Math.add(10,20)