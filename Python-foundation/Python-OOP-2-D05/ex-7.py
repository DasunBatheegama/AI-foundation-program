class Box:
    def __init__(self, width=0, height=0, length=0, name=""):
        print("Box created", width, height, length)
        self.width = width
        self.height = height
        self.length = length
        self.name = name

    def volume(self):
        return self.length * self.width * self.height

b1 = Box(30, 10)
b1.name = "Box 1"
print("Box Name :", b1.name)
print("Box Volume :", b1.volume())

