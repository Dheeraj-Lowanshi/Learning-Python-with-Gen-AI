class Manager:
    def review(self):
        print("Final review done by manager")

class Reviewer(Manager):
    def review(self):
        print("Reviewing done by reviewer")
        super().review()

class Developer(Reviewer):
    def review(self):
        print("Code reviewing by developer")
        super().review()

obj=Developer()
obj.review()