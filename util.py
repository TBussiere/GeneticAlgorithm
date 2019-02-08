import pybullet as p
import time
import random
import Shape as s


def initSim(nbobj, rad, pos1):
    # créé le sol
    p.createCollisionShape(p.GEOM_PLANE)
    basePlane = p.createMultiBody(0, 0)
    # met une seed au rng
    random.seed(time.time())
    # random.seed("Thibault")
    # créé la sphere qui sera le point centrale de la "Shape"
    nbPop = 10
    pop = []
    for i in range(0,nbPop-1):
        body = p.createCollisionShape(p.GEOM_SPHERE, radius=rad*4)
        temp = s.Shape(body, pos1)
        temp.createRandom(nbobj, rad)
        idtmp = temp.createBody()
        pop.append(temp)

        pop[i].setId(idtmp)
    
    for elem1 in range(0,nbPop-1):
        for elem2 in range(elem1+1,nbPop-1):
            for i in range(-1,nbobj):
                for j in range(-1,nbobj):
                    p.setCollisionFilterPair(pop[elem1].getId(), pop[elem2].getId(), i,j, 0)

    
    # ==========================================================
    # Truc lié a la simulation
    # ==========================================================
    for elem in pop:
        for i in range(0, nbobj):
            p.setJointMotorControl2(bodyUniqueId=elem.getId(), jointIndex=i,
                                    controlMode=p.VELOCITY_CONTROL,
                                    targetVelocity=random.randint(0, 3))
                                

    # met la gravité
    p.setGravity(0, 0, -9.81)

    return pop
