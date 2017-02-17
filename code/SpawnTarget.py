import mcpi.minecraft as minecraft
import mcpi.block as block
from mine import Vec3
import text
from random import randint

mc = minecraft.Minecraft.create()
position = mc.player.getPos()

colour0 = 'red'
colour1 = 'white'

BlockType0 = eval("block.WOOL_{}".format(colour0.upper()));
BlockType1 = eval("block.WOOL_{}".format(colour1.upper()));

BlockType = [BlockType0, BlockType1]

rot = mc.player.getRotation() - 90
forward = text.angleToTextDirectionCardinal(rot)

print(rot)

for i in range(-2, 2+1):
	for j in range(-2, 2+1):
		if (rot < 45 and rot >-45) or (rot > -225 and rot < -125):
			BlockRelativeLoc = Vec3(0,j,i)
		else:
			BlockRelativeLoc = Vec3(i,j,0)
		if ((i+j)%2 != 0) and not (abs(i) == 2 or abs(j) == 2):
			mc.setBlock(position+forward*20+BlockRelativeLoc, BlockType[1])
		elif (abs(i)==abs(j) and abs(i)==1):
			mc.setBlock(position+forward*20+BlockRelativeLoc, BlockType[1])
		else:
			mc.setBlock(position+forward*20+BlockRelativeLoc, BlockType[0])
