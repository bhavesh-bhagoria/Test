def cube(a,op):
    area_of_cube = 6*(a)**2
    vol_of_cube = a**3
    return area_of_cube,vol_of_cube
def cuboid(l,b,h,op):
    area_of_cuboid = 2*(l*b + b*h + l*h)
    vol_of_cuboid = l*b*h
    return area_of_cuboid,vol_of_cuboid 
def sphere(r,op):
    area_of_sphere = 4*(22/7)*(r)**2
    vol_of_sphere = (4/3)*(22/7)*(r)**3
    return area_of_sphere,vol_of_sphere
op = input("enter shape: cube/cuboid/sphere: ")
if op.lower() == "cube":
    a = float(input("enter side of cube: "))
    area_cube,vol_cube = cube(a,op)
    print("area_of_cube: ", area_cube)
    print("vol_of_cube: ", vol_cube)
elif op.lower() == "cuboid":
    l = float(input("enter length of cuboid: "))
    b = float(input("enter breadth of cuboid: "))
    h = float(input("enter height of cuboid: "))
    area_cuboid,vol_cuboid = cuboid(l,b,h,op)
    print("area_of_cuboid: ", area_cuboid)
    print("vol_of_cuboid: ", vol_cuboid)
elif op.lower() == "sphere":
    r = float(input("enter radius of sphere: "))
    area_sphere,vol_sphere = sphere(r,op)   
    print("area_of_sphere: ", area_of_sphere)
    print("vol_of_sphere: ", vol_of_sphere)
else:
    print("Invalid INPUT")









