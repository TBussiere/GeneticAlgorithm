import pybullet as p
import time
import random


p.connect(p.GUI)
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)


random.seed(time.time)

nbobj = 5

rad = 0.05
ratation = [0, 0, 0, 1]
pos1 = [10*rad, 10*rad, 10*rad]

body = p.createCollisionShape(p.GEOM_SPHERE, radius=rad)
colBoxId = p.createCollisionShape(
    p.GEOM_BOX, halfExtents=[rad, rad, rad])

# parts = []
mass = 1

linkMass = []
linkColind = []
linkpos = []
linkRotate = []
idk1 = []
idk2 = []
vShapeInd = []
# l'objet 0(carré) est link au 0 du main body (boule)
linkInd = []
# p.JOINT_PRISMATIC
# p.JOINT_REVOLUTE
joinType = []
joinAxis = []


for i in range(0, nbobj):

    print("-----------------------")
    print(i)

    rng = random.randint(0, 1)

    if rng == 1:
        linkColind.append(p.createCollisionShape(
            p.GEOM_BOX, halfExtents=[rad, rad, rad]))
    else:
        linkColind.append(p.createCollisionShape(
            p.GEOM_SPHERE, radius=rad))

    linkMass.append(mass)
    linkpos.append([random.randint(0, 100)/100,
                    random.randint(0, 100)/100, random.randint(0, 100)/100])
    linkRotate.append([0, 0, 0, 1])
    idk1.append([0, 0, 0])
    idk2.append([0, 0, 0, 1])
    vShapeInd.append(-1)
    linkInd.append(random.randint(0, i))

    rng = random.randint(0, 1)
    if rng == 1:
        joinType.append(p.JOINT_PRISMATIC)
    else:
        joinType.append(p.JOINT_REVOLUTE)

    joinAxis.append(
        [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)])


shape = p.createMultiBody(body, mass, -1, pos1, ratation,
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


p.setGravity(0, 0, -7)
p.setRealTimeSimulation(1)
while (1):
    keys = p.getKeyboardEvents()
    time.sleep(0.5)


"""
OLD

nb_links = nbobj
linkMass = [0.1]
linkColind = [colBoxId]

linkpos = [[1, 0, 0]]
linkRotate = [[0, 0, 0, 1]] * nb_links
idk1 = [[0, 0, 0]] * nb_links
idk2 = [[0, 0, 0, 1]] * nb_links
vShapeInd = [-1] * nb_links
# l'objet 0(carré) est link au 0 du main body (boule)
linkInd = [0]
# p.JOINT_PRISMATIC
# p.JOINT_REVOLUTE
#
joinType = [p.JOINT_PRISMATIC]
joinAxis = [[1, 0, 0]]
"""
