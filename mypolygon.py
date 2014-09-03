#!/usr/bin/python
# Filename:mypolygon.py

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob

def square(t, dist):
    for i in range(4):
        fd(t,dist)
        lt(t)

bob.delay = 0.01

def polygon(t, dist, n):
    for i in range(n):
        fd(t,dist)
        lt(t, 360.0/n)

def ployline(t, dist, n, angle):
    """Draws n line segments with the given length and 
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        fd(t, dist)
        lt(t, angle)

def arc(t, r, angle):
    """Draws a part of a circle with the given r and 
    angle (in degrees). t is a turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    ployline(t, step_length, n, step_angle)

def circle(t, r):
    arc(t, r, 360)

# square(bob, 100)
# polygon(bob, 30, 5)

#arc(bob, 40, 60)
#circle(bob, 40)

#wait_for_user()

