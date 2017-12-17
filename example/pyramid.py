# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:53:11 2017

@author: Sam0225
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
height = 10
base = (10-1)*2 

for i in range(height):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i
    
    x2 = pos.x + base - i
    #y與y2相同
    z2 = pos.z + base - i
    mc.setBlocks(x, y, z, x2, y, z2, 24)

