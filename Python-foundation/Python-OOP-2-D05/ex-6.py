class Box:
    width = 0
    height = 0
    length = 0

    def __init__(self, width, height, length):
        print("Box created", width, height, length)
        self.width = width
        self.height = height
        self.length = length

    def volume(self):
        return self.length * self.width * self.height

b0. Box(10, 20, 30)
print(b0.name)

b1 = Box(30, 10, 20)
b1.name = "Box 1"
print("Box Name :", b1.name)
print("Box Volume :", b1.volume())

