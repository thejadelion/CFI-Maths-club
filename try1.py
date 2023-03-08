import random
import math as m

n_particles = 1000
csys = []
for i in range(n_particles):
    csys.append([random.random(), random.random()])

velocities = []
t = float(input("Enter the temperature: "))
for i in range(n_particles):
    vx = random.random()
    vy = random.random()
    v1 = m.sqrt(vx**2+vy**2)
    vx, vy = m.sqrt(t)*vx/v1, m.sqrt(t)*vy/v1
    velocities.append([vx, vy])

def iterate(csys, velocities, dt):
    # This function is to update the position of the particle in each iteration, taking into account boundaries
        for i in range(n_particles):
        csys[i][0] = velocities[i][0] * dt + csys[i][0]
        csys[i][1] = velocities[i][1] * dt + csys[i][1]
        if csys[i][0]>1:
            csys[i][0] = 2 - csys[i][0]
            velocities[i][0]=-velocities[i][0]
        if csys[i][1]>1:
            csys[i][1] = 2 - csys[i][1]
            velocities[i][1] = -velocities[i][1]
        if csys[i][0]<0:
            csys[i][0] = - csys[i][0]
            velocities[i][0] = -velocities[i][0]
        if csys[i][1]<0:
            csys[i][1] = - csys[i][1]
            velocities[i][1] = -velocities[i][1]
    return csys

def collide(csys1, csys2):
    # This function is to update the number of collisions in each iteration.
    # Removing the particles which have already collided (maybe with probability)
    pass
    return n

def controller():
    tnow = 0
    dt = 0.0001
    t = float(input("Enter the timescale"))
    collisions = 0

    while tnow < t:
        iterate()
        cin = collisions
        collisions += collide()
        tnow += dt
        print(collisions, tnow, (-cin+collisions)/dt)


    print("Average collision rate is", collisions/tnow)
print(csys)
