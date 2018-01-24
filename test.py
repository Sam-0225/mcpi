#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:46:03 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()
mc.setBlocks(pos.x+30, pos.y+30, pos.z+30, pos.x-30, pos.y-30, pos.z-30, 0 )








"""
hits = mc.events.pollBlockHits()
block = 103

for hit in hits:
    x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
    mc.setBlock(x,y,z, block)
"""
"""
blocks=[]
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        hitX, hitY, hitZ = hit.pos.x, hit.pos.y, hit.pos.z
        mc.setBlock(hitX,hitY,hitZ, 41)
"""
"""
while True:
 
    for blockhit in mc.player.pollBlockHits():
        pos = blockhit.pos
        gold_block_id = 41
        mc.setBlock(pos.x, pos.y, pos.z, gold_block_id)
 
    time.sleep(1)
"""