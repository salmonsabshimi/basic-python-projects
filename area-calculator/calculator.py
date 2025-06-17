import math

print('=================')
print('Area Calculator 📐')
print('=================')
print()
print(' 1) Triangle\n 2) Rectangle \n 3) Square \n 4) Circle \n 5) Quit')
print()
shape_choice = int(input('Which shape: '))
print()

# triangle
if shape_choice == 1: 
  base = float(input("Base: "))
  height = float(input("Height: "))
  area = 0.5 * base * height 
  print()
  print("The area of the triangle is:", area)

# rectangle
elif shape_choice == 2: 
  base = float(input("Length: "))
  width = float(input("Width: "))
  area = base * width
  print()
  print("The area of the rectangle is:", area)

# square
elif shape_choice == 3: 
  side = float(input("Length: "))
  area = side **2
  print()
  print("The area of the square is:", area)

# circle
elif shape_choice == 4: 
  radius = float(input("Radius: "))
  area = radius**2 * math.pi 
  print()
  print("The area of the circle is:", area)

# quit
elif shape_choice == 5: 
  print("Quit")

else: 
  print("Invalid selection")
