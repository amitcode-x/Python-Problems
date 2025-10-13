# --------------------------------------------------------Multiple Inheritance Example---------------------------------------------------



#parent 1
class Camera:
    def take_photo(self):
        print("Taking photo...")

#parent 2
class Phone:
    def make_call(self):
        print("Making a call...")
#child
class SmartPhone(Camera, Phone):
    def browse(self):
        print("Browsing the internet...")

sp = SmartPhone()
sp.take_photo()
sp.make_call()
sp.browse()