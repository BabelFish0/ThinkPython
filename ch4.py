# %%
import math
import turtle
turt = turtle.Turtle()
# %% [markdown]
# ex 4-2
# %%
#turt.fd(200)
# %%
def curve(t, segments, length, angle):
    lenPerSeg = length/segments
    for n in range(segments):
        t.forward(lenPerSeg)
        t.right(angle)
# %%
def arc(t, radius, angle):
    arcLength = (math.pi * 2 * radius)*(angle/360)
    segments = int(arcLength/10) + 2
    anglePerSeg = angle/segments
    curve(t, segments, arcLength, anglePerSeg)
# %%
def petal(t, radius, angle):
    arc(t, radius, angle)
    t.right(180-angle)
    arc(t, radius, angle)
# %%
def flower(t, petals, radius, angle):
    angleOffset = 360/petals+180-angle
    for p in range(petals):
        petal(t, radius, angle)
        t.right(angleOffset)
# %%
turt.speed(0)
#curve(turt, 10, 200, 5)
#arc(turt, 200, 270)
#petal(turt, 200, 120)
#flower(turt, 30, 200, 40)
#turtle.mainloop()
# %% [markdown]
# ex 4-3
# %%
def isoTri(t, topAngle, base):
    baseAngle = 0.5*(math.pi-topAngle)
    sideLength = math.sin(baseAngle)*(base/math.sin(topAngle))
    t.forward(sideLength)
    t.left(360*((math.pi-baseAngle)/(2*math.pi)))
    t.forward(base)
    t.left(360*((math.pi-baseAngle)/(2*math.pi)))
    t.forward(sideLength)
# %%
def polygon(t, sides, sideLength):
    for n in range(sides):
        isoTri(t, (2*math.pi)/sides, sideLength)
        t.right(180)
# %%
#isoTri(turt, 1.8, 500)
polygon(turt, 60, 10)
turtle.mainloop()
# %%
