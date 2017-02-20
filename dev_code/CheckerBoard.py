import mcpi.minecraft as minecraft
import mcpi.block as block
from mine import Vec3
import text
from random import randint

mc = minecraft.Minecraft.create()
position = mc.player.getPos()

colour1 = 'red'
colour2 = 'white'

BlockType1 = eval("block.WOOL_{}".format(colour1.upper()));
BlockType2 = eval("block.WOOL_{}".format(colour2.upper()));

BlockType = [BlockType1, BlockType2]

rot = mc.player.getRotation() - 90
forward = text.angleToTextDirectionCardinal(rot)

for i in range(-4, 4):
	for j in range(-4, 4):
		BlockRelativeLoc = Vec3(i,-1,j)
		if ((i+j)%2 != 0):
			mc.setBlock(position+forward*20+BlockRelativeLoc, BlockType[1])
		else:
			mc.setBlock(position+forward*20+BlockRelativeLoc, BlockType[0])