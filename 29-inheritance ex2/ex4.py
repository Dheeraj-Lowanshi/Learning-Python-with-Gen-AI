class Phone:
    def make_call(self):
        print("Making a call....")

class Computer:
    def browse_internet(self):
        print("Browsing the internet...")

class SmartPhone(Phone,Computer):
    def take_photo(self):
        print("Taking a photo using camera...")

apple=SmartPhone()
apple.make_call()
apple.browse_internet()
apple.take_photo()
