import pybullet as p
import numpy as np
import time
import Shape as s
import util


# créé la fenetre de base
p.connect(p.GUI)
# Defini le nombre d'objet pour la "RandomShape"
nbobj = 4
# defini un radius de base
rad = 0.05
# defini une mass de base
mass = 1
# defini une rotation de base
rotation = [0, 0, 0, 1]
# defini une position de base
pos1 = [0, 0, 2]
basex = pos1[0]
basey = pos1[1]
basez = pos1[2]

# shape est un tab
shape = util.initSim(nbobj, rad, pos1)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
maxFit = 0

# met la simulation en mode real time
p.setRealTimeSimulation(1)
fastForward = False
p.setPhysicsEngineParameter(maxNumCmdPer1ms=1000)

# Le "run"
while (1):
    rkey = ord('r')
    fkey = ord('f')
    nkey = ord('n')
    keys = p.getKeyboardEvents()
    if rkey in keys and keys[rkey] & p.KEY_WAS_TRIGGERED:
        p.resetSimulation()
        p.setRealTimeSimulation(0)
        shape = util.initSim(nbobj, rad, pos1)
        p.setRealTimeSimulation(1)
        maxFit = 0
        continue
    elif fkey in keys and keys[fkey] & p.KEY_WAS_TRIGGERED:
        if fastForward:
            fastForward = False
            p.setRealTimeSimulation(1)
        else:
            fastForward = True
            p.setRealTimeSimulation(0)
    elif nkey in keys and keys[nkey] & p.KEY_WAS_TRIGGERED:
        p.resetSimulation()
        p.setRealTimeSimulation(0)
        shape = util.nextGen(nbobj, rad, pos1, shape)
        p.setRealTimeSimulation(1)
        maxFit = 0
        continue

    posbody = p.getBasePositionAndOrientation(shape[0].getId())[0]
    curCam = p.getDebugVisualizerCamera()
    p.resetDebugVisualizerCamera(
        cameraDistance=curCam[10], cameraYaw=curCam[8],
        cameraPitch=curCam[9],
        cameraTargetPosition=posbody)

    curx = posbody[0]
    cury = posbody[1]
    curz = posbody[2]

    fitness = (np.abs(curx-basex) + np.abs(cury-basey))

    if maxFit < fitness:
        maxFit = fitness
        # print(maxFit)

    if fastForward:
        p.stepSimulation()
        # time.sleep(1/1000)
    else:
        time.sleep(1/60)
