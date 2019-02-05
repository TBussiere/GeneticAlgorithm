import pybullet as p
import random


class Shape:
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
    # Exemple [0,1] => Link 0 qui est le body avec 0+1 qui
    # est le 1er objet generé
    #               Et Link le 1er objet genéré avec le second
    linkInd = []
    # p.JOINT_REVOLUTE
    joinType = []
    # defini les axes de liberté du join defini avant
    joinAxis = []

    nbobj = 0

    shapeId = -1

    def __init__(self, body, pos=[0, 0, 0], mass=1, rota=[0, 0, 0, 1]):
        self.baseMass = mass
        self.body = body
        self.basePos = pos
        self.baseRota = rota

    def addLink(self, mass, colInd, pos, linkind, joinAxis):
        self.linkMass.append(mass)
        self.linkColind.append(colInd)
        self.linkpos.append(pos)
        self.linkInd.append(linkind)
        self.joinAxis.append(joinAxis)

        self.linkRotate.append(self.baseRota)
        self.idk1.append([0, 0, 0])
        self.idk2.append([0, 0, 0, 1])
        self.vShapeInd.append(-1)
        self.joinType.append(p.JOINT_REVOLUTE)

        self.nbobj = self.nbobj + 1

    def createBody(self):

        res = p.createMultiBody(self.body, self.baseMass, -1, self.basePos,
                                self.baseRota,
                                linkMasses=self.linkMass,
                                linkCollisionShapeIndices=self.linkColind,
                                linkPositions=self.linkpos,
                                linkOrientations=self.linkRotate,
                                linkParentIndices=self.linkInd,
                                linkJointTypes=self.joinType,
                                linkJointAxis=self.joinAxis,
                                linkVisualShapeIndices=self.vShapeInd,
                                linkInertialFramePositions=self.idk1,
                                linkInertialFrameOrientations=self.idk2
                                )
        return res

    def createRandom(self, nbobj, echelle):

        for i in range(0, nbobj):
            rng = random.randint(0, 1)
            # cs
            if rng == 1:
                test1 = echelle * random.randint(1, 5)
                test2 = echelle * random.randint(1, 5)
                test3 = echelle * random.randint(1, 5)
                cs = p.createCollisionShape(
                    p.GEOM_BOX, halfExtents=[test1, test2, test3])
            else:
                test = echelle * random.randint(1, 5)
                cs = p.createCollisionShape(p.GEOM_SPHERE, radius=test)

            # [tempx, tempy, tempz]
            tempx = random.randint(1, 100)/250
            tempy = random.randint(1, 100)/250
            tempz = random.randint(1, 100)/250

            # ind
            ind = random.randint(0, i)

            # [axis1,axis2,axis3]
            axis1 = random.randint(0, 1)
            axis2 = random.randint(0, 1)
            axis3 = random.randint(0, 1)
            if axis1 == 0 and axis2 == 0 and axis3 == 0:
                while axis1 == 0 and axis2 == 0 and axis3 == 0:
                    axis1 = random.randint(0, 1)
                    axis2 = random.randint(0, 1)
                    axis3 = random.randint(0, 1)
            self.addLink(self.baseMass, cs, [tempx, tempy, tempz], ind, [
                axis1, axis2, axis3])

    """
    Faire Mutate
    """
    def mutate():
        pass

    """
    Faire Mutate
    """
    def crossOver(other):
        pass
