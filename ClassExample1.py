
class Demo:

    def __init__(self):
        print("Init method")
    def sample(self):
        print("Sample Method")

dem=Demo()
print(type(dem))

Demo.sample(dem)

dem.sample()