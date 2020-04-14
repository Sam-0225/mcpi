import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

def drawBuilding(locx, locy, locz, floors, width, depth, floorheight, wallmaterial, floormaterial):
    topx = locx + width
    topy = locy + ((floorheight + 1) * floors)
    topz = locz + depth

    mc.setBlocks(locx, locy, locz, topx, topy, topz, wallmaterial)
    mc.setBlocks(locx + 1, locy + 1, locz + 1, topx - 1, topy - 1, topz - 1, 0)

    if floors > 1:
        for i in range(floors - 1):
            floorYloc = locy + ((floorheight + 1) * (i + 1))
            mc.setBlocks(locx + 1, floorYloc, locz + 1, topx - 1, floorYloc, topz - 1, floormaterial)

    doorloc = random.randint(1, width - 2)
    mc.setBlock(locx, locy + 1, locz + doorloc, 0)
    mc.setBlock(locx, locy + 2, locz + doorloc, 0)

    if floors > 1:
        for i in range(floors - 1):
            windowYloc = locy + 2 + ((floorheight + 1) * (i + 1))
            for j in range(floorheight - 1):
                mc.setBlocks(locx, windowYloc + j, locz + 1, locx, windowYloc + j, locz + (width - 1), 102)

    if floors > 1:
        for i in range(floors - 1):
            windowYloc = locy + 2 + ((floorheight + 1) * (i + 1))
            for j in range(floorheight - 1):
                mc.setBlocks(locx + depth, windowYloc + j, locz + 1, locx + depth, windowYloc + j, locz + width - 1, 102)

drawBuilding(x,y,z, 5, 5, 5, 3, 1, 5)
