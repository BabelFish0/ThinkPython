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
    angleOffset = 360/petals
    for p in range(petals):
        petal(t, radius, angle)
        t.right(angleOffset)
# %%
#curve(turt, 10, 200, 5)
#arc(turt, 200, 270)
petal(turt, 200, 120)
#flower(turt, 10, 200, 60)
turtle.mainloop()
# %%

# %%
