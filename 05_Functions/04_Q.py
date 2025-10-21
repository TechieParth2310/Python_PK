# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math
def function(r):
    area = math.pi*r**2
    circum = 2*math.pi*r

    return round(area,2),round(circum,2)

a,c = function(5)
print("area: ",a,"circumference: ",c)