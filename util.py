import pybullet as p
import time
import random
import Shape as s


def initSim(nbobj, rad, pos1):
    # créé le sol
    p.createCollisionShape(p.GEOM_PLANE)
    p.createMultiBody(0, 0)
    # met une seed au rng
    random.seed(time.time())
    # random.seed("Thibault")
    # créé la sphere qui sera le point centrale de la "Shape"
    body = p.createCollisionShape(p.GEOM_SPHERE, radius=rad*4)

    aShape = s.Shape(body, pos1)

    # ==========================================================
    # Generation des nouvelles shapes
    # ==========================================================
    aShape.createRandom(nbobj, rad)

    # ==========================================================
    # Creation du Multi Body Aka Le truc qui bouge
    # ==========================================================
    shape = aShape.createBody()

    if shape == -1:
        print("ERROR BUILDING SHAPE !!!")
        p.disconnect()

    # ==========================================================
    # Truc lié a la simulation
    # ==========================================================

    for i in range(0, nbobj):
        p.setJointMotorControl2(bodyUniqueId=shape, jointIndex=i,
                                controlMode=p.VELOCITY_CONTROL,
                                targetVelocity=random.randint(0, 3))

    # met la gravité
    p.setGravity(0, 0, -10)

    return shape
