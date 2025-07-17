def find_cylinder_volume(radius,height):
    print("height:", height)
    print("radius:", radius)
    volume = 3.14*(radius**2)*height
    return volume
r = 10
h = 12
v = find_cylinder_volume(r,h)
print(v)