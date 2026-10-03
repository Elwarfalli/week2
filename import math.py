import math
print(dir(math))

help(math)

help(math.sqrt)

import math

print("Things available in the math library:")
print(dir(math))

print("\nValue of pi:")
print(math.pi)

print("\nSquare root of 25:")
print(math.sqrt(25))

print("\nCosine of 0:")
print(math.cos(0))


import math

angle_degrees = float(input("Enter an angle in degrees: "))

angle_radians = math.radians(angle_degrees)

print("Degrees:", angle_degrees)
print("Radians:", angle_radians)


temperature = float(input("Enter the temperature: "))

if temperature > 100:
    print("Temperature is high.")
else:
    print("Temperature is normal.")



