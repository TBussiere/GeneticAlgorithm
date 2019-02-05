import pybullet as p
import numpy as np
import time
import random
import Shape as s

# créé la fenetre de base
p.connect(p.GUI)
# créé le sol
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)
# met une seed au rng
random.seed(time.time())
# Defini le nombre d'objet pour la "RandomShape"
nbobj = 5

# defini un radius de base
rad = 0.05
# defini une mass de base
mass = 1
# defini une rotation de base
rotation = [0, 0, 0, 1]
# defini une position de base
pos1 = [0, 0, 2]
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
# enleve la pause
p.setRealTimeSimulation(1)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

basex = pos1[0]
basey = pos1[1]
basez = pos1[2]

maxFit = 0

cyaw = 10
cpitch = -15
cdist = 5

# Le "run"
while (1):
    # keys = p.getKeyboardEvents()

    posbody = p.getBasePositionAndOrientation(body)[0]
    p.resetDebugVisualizerCamera(
        cameraDistance=cdist, cameraYaw=cyaw, cameraPitch=cpitch,
        cameraTargetPosition=posbody)

    curx = posbody[0]
    cury = posbody[1]
    curz = posbody[2]

    fitness = (np.abs(curx-basex) + np.abs(cury-basey))

    if maxFit < fitness:
        maxFit = fitness

    # print(maxFit)

    time.sleep(1/65)


p.disconnect()
