class Manager:
    def final_review(self):
        print("Final review done by manager")

class Reviewer(Manager):
    def review(self):
        print("Reviewing done by reviewer")

class Developer(Reviewer):
    def write_code(self):
        print("Code written by developer")

obj=Developer()
obj.write_code()
obj.review()
obj.final_review()