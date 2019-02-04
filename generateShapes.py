import pybullet as p
import time
import random

# créé la fenetre de base
p.connect(p.GUI)
# créé le sol
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)
# met une seed au rng
random.seed(time.time)
# Defini le nombre d'objet pour la "RandomShape"
nbobj = 5

# defini un radius de base
rad = 0.05
# defini une mass de base
mass = 1
# defini une rotation de base
ratation = [0, 0, 0, 1]
# defini une position de base
pos1 = [10*rad, 10*rad, 10*rad]
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

    print("-----------------------")
    print(i)

    rng =0# random.randint(0, 1)

    if rng == 1:
        test1 = rad * random.randint(1,5)
        test2 = rad * random.randint(1,5)
        test3 = rad * random.randint(1,5)
        linkColind.append(p.createCollisionShape(
            p.GEOM_BOX, halfExtents=[test1, test2, test3]))
    else:
        test = rad * random.randint(1,5)
        linkColind.append(p.createCollisionShape(
            p.GEOM_SPHERE, radius=test))

    linkMass.append(mass)
    linkpos.append([random.randint(0, 100)/250,
                    random.randint(0, 100)/258, random.randint(0, 100)/250])
    linkRotate.append([0, 0, 0, 1])
    idk1.append([0, 0, 0])
    idk2.append([0, 0, 0, 1])
    vShapeInd.append(-1)
    linkInd.append(random.randint(0, i))
    joinType.append(p.JOINT_REVOLUTE)

    joinAxis.append(
        [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)])

# ==========================================================
# Creation du Multi Body Aka Le truc qui devra bouger
# ==========================================================
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


# ==========================================================
# Truc lié a la simulation
# ==========================================================


for i in range(0,nbobj):
   p.setJointMotorControl2(bodyUniqueId=shape,jointIndex=i,controlMode=p.VELOCITY_CONTROL,targetVelocity=random.randint(0,5))



# met la gravité
p.setGravity(0, 0, -0.01)
# enleve la pause
p.setRealTimeSimulation(1)
# Le "run"
while (1):
    keys = p.getKeyboardEvents()
    time.sleep(1.2)


p.disconnect()