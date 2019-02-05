import pybullet as p


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

    def __init__(self, body, mass=1, pos=[0, 0, 0], rota=[0, 0, 0, 1]):
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

    def createBody(self, mass, colInd, pos, linkind, joinAxis):

        res = p.createMultiBody(self.body, mass, -1, self.basePos,
                                self.baseRota,
                                linkMasses=self.linkMass,
                                linkCollisionShapeIndices=self.linkColind,
                                linkPositions=self.linkpos,
                                linkOrientations=self.linkRotate,
                                linkParentIndices=self.linkInd,
                                linkJointTypes=self.self.joinType,
                                linkJointAxis=self.joinAxis,
                                linkVisualShapeIndices=self.vShapeInd,
                                linkInertialFramePositions=self.idk1,
                                linkInertialFrameOrientations=self.idk2
                                )
        return res

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
