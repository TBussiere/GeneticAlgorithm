import pybullet as p
import numpy as np
import time
import random

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

# ==========================================================
# Creation des matrices pour link les autres shapes au body
# ==========================================================
# poid du nouveau l'objet
linkMass = []
# CollisionShape du nouveau objet
linkColind = []
# position relative du nouveau objet
linkpos = []
# oriantation du nouveau objet
linkRotate = []
# je sais pas trop a quoi sa sert mais si on le met pas sa plante
idk1 = []
# je sais pas trop a quoi sa sert mais si on le met pas sa plante
idk2 = []
# defini une texture -1 pour pas default
vShapeInd = []
# l'objet index i est link au chiffre n+1 mis dans la liste
# Exemple [0,1] => Link 0 qui est le body avec 0+1 qui est le 1er objet generé
#               Et Link le 1er objet genéré avec le second
linkInd = []
# acepte une emum de la lib exemple :
# p.JOINT_PRISMATIC
# p.JOINT_REVOLUTE
joinType = []
# defini les axes de liberté du join defini avant
joinAxis = []

# ==========================================================
# Generation des nouvelles shapes
# ==========================================================

for i in range(0, nbobj):

    rng = random.randint(0, 1)

    if rng == 1:
        test1 = rad * random.randint(1, 5)
        test2 = rad * random.randint(1, 5)
        test3 = rad * random.randint(1, 5)
        linkColind.append(p.createCollisionShape(
            p.GEOM_BOX, halfExtents=[test1, test2, test3]))
    else:
        test = rad * random.randint(1, 5)
        linkColind.append(p.createCollisionShape(
            p.GEOM_SPHERE, radius=test))

    linkMass.append(mass)
    tempx = random.randint(1, 100)/250
    tempy = random.randint(1, 100)/250
    tempz = random.randint(1, 100)/250
    linkpos.append([tempx, tempy, tempz])
    linkRotate.append([0, 0, 0, 1])
    idk1.append([0, 0, 0])
    idk2.append([0, 0, 0, 1])
    vShapeInd.append(-1)
    ind = random.randint(0, i)
    linkInd.append(ind)
    joinType.append(p.JOINT_REVOLUTE)

    axis1 = random.randint(0, 1)
    axis2 = random.randint(0, 1)
    axis3 = random.randint(0, 1)
    if axis1 == 0 and axis2 == 0 and axis3 == 0:
        while axis1 == 0 and axis2 == 0 and axis3 == 0:
            axis1 = random.randint(0, 1)
            axis2 = random.randint(0, 1)
            axis3 = random.randint(0, 1)
    joinAxis.append(
        [axis1, axis2, axis3])

# ==========================================================
# Creation du Multi Body Aka Le truc qui devra bouger
# ==========================================================
shape = p.createMultiBody(body, mass, -1, pos1, rotation,
                          linkMasses=linkMass,
                          linkCollisionShapeIndices=linkColind,
                          linkPositions=linkpos,
                          linkOrientations=linkRotate,
                          linkParentIndices=linkInd,
                          linkJointTypes=joinType,
                          linkJointAxis=joinAxis,
                          linkVisualShapeIndices=vShapeInd,
                          linkInertialFramePositions=idk1,
                          linkInertialFrameOrientations=idk2
                          )

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
