from vpython import *

scene = canvas(title="3D Sphere")

ball = sphere(pos=vector(0, 0, 0), radius=1, color=color.blue)


while True:
    rate(30)
    ball.rotate(angle=0.01, axis=vector(0, 1, 0))

    