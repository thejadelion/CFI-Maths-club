import random
import math



def iterate(csys, velocities, dt):
    # This function is to update the position of the particle in each iteration, taking into account boundaries
    for i in range(n_particles):
        csys[i][0] = velocities[i][0] * dt + csys[i][0]
        csys[i][1] = velocities[i][1] * dt + csys[i][1]
        if csys[i][0] > 1:
            csys[i][0] = 2 - csys[i][0]
            velocities[i][0] =- velocities[i][0]
        if csys[i][1] > 1:
            csys[i][1] = 2 - csys[i][1]
            velocities[i][1] = -velocities[i][1]
        if csys[i][2] > 1:
            csys[i][2] = 2 - csys[i][2]
            velocities[i][1] = -velocities[i][1]
        if csys[i][0] < 0:
            csys[i][0] = - csys[i][0]
            velocities[i][0] = -velocities[i][0]
        if csys[i][1] < 0:
            csys[i][1] = - csys[i][1]
            velocities[i][1] = -velocities[i][1]
        if csys[i][2] < 0:
            csys[i][2] = - csys[i][1]
            velocities[i][2] = -velocities[i][2]
    return csys



def collide(csys1, csys2):
    # This function is to update the number of collisions in each iteration.
    # Removing the particles which have already collided (maybe with probability)
    count = 0
    clist = []
    global n_particles
    for i in range(n_particles):
        for j in range(i):
            if math.dist(csys1[i], csys1[j]) < 2*r or math.dist(csys2[i], csys2[j]) < 2*r:
                count += 1
                d = random.random()
                if d < 0.4:
                    if i not in clist:
                        clist.append(i)
                    if j not in clist:
                        clist.append(j)
    ctr = 0
    n_particles -= len(clist)
    for i in clist:
        csys2.pop(i-ctr)
        ctr += 1
    return count

def controller(t):
    tnow = 0
    dt = 0.0001
    collisions = 0

    while tnow < t:
        csys1 = list(csys)
        iterate(csys, velocities, dt)
        csys2 = csys
        cin = collisions
        collisions += collide(csys1, csys2)
        tnow += dt
    return collisions/tnow


for i1 in range(1, 100):
    t = 10*i1
    r = 0.02
    n_particles = 500
    csys = []
    for i in range(n_particles):
        csys.append([random.random(), random.random(), random.random()])

    velocities = []
    for i in range(n_particles):
        vx = random.gauss(math.sqrt(t), 0.47*math.sqrt(t))
        if math.fabs(vx) > 100:
            vx = 100 * vx/math.fabs(vx)
        vy = random.gauss(math.sqrt(t), 0.47*math.sqrt(t))
        if math.fabs(vy) > 100:
            vy = 100 *vy/math.fabs(vy)
        vz = random.gauss(math.sqrt(t), 0.47 * math.sqrt(t))
        if math.fabs(vz) > 100:
            vz = 100 * vz / math.fabs(vy)
        v1 = math.sqrt(vx ** 2 + vy ** 2 + vz**2)
        vx, vy, vz = math.sqrt(t) * vx / v1, math.sqrt(t) * vy / v1, math.sqrt(t) * vz / v1
        velocities.append([vx, vy, vz])

    print(t, controller(0.01))

