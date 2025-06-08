from vpython import *

floor = box(pos=vector(0, -2, 0), size=vector(10, 0.5, 10), color=color.green)
body = box(pos=vector(0, 0, 0), size=vector(2, 3, 1), color=color.red)
head = sphere(pos=vector(0, 2.5, 0), radius=0.8, color=color.yellow)
left_arm = cylinder(pos=vector(-1.5, 0.8, 0), axis=vector(-1, 0, 0), radius=0.2, length=1, color=color.blue)
right_arm = cylinder(pos=vector(1.5, 0.8, 0), axis=vector(1, 0, 0), radius=0.2, length=1, color=color.blue)
left_leg = cylinder(pos=vector(-0.5, -2, 0), axis=vector(0, -1, 0), radius=0.2, length=1.5, color=color.orange)
right_leg = cylinder(pos=vector(0.5, -2, 0), axis=vector(0, -1, 0), radius=0.2, length=1.5, color=color.orange)

while True:
    rate(60)
