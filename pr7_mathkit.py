
import math

def factorial_of(n):
    return 1 if n<=1 else n*factorial_of(n-1)

def compound_interest(p, r, t):
    return round(p * ((1 + r/100.0) ** t), 2)

def trig_values(angle_deg):
    rad = math.radians(angle_deg)
    return round(math.sin(rad),4), round(math.cos(rad),4), round(math.tan(rad),4)

def area_shapes(shape, *args):
    if shape=="circle":
        return round(math.pi * args[0]**2, 2)
    if shape=="rect":
        return args[0]*args[1]
    if shape=="tri":
        return 0.5*args[0]*args[1]
    return None
