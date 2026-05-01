def volume(length, width, height):
    return length * width * height

def area(length, width):
    return length * width

def box_surface_area(length, width, height):
    return area(length, width) * 2 + area(width, height) * 2 + area(height, length) * 2

def box_details(length, width, height):
    box_volume = volume(length, width, height)
    box_area = box_surface_area(length, width, height)
    print("Box details:", f"length = {length}, Width = {width}, height = {height}")
    print("volume:", box_volume)
    print("surface area:", box_area)
    print("\n")

box_details(10, 20, 30)
box_details(20, 6.7, 8.9)

# length, width, heigtht = 10, 20, 30
# box_1_volume = volume(length, width, heigtht)
# box_1_area = box_surface_area(length, width, heigtht)
# print(box_1_volume) 
# print(box_1_area)

# box_2_volume = volume(20, 6.7, 8.9)
# print(box_2_volume)

# box_3_volume = volume(20, 20, 20)
# print(box_3_volume)