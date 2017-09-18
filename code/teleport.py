import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
dire = mc.player.getDirection()

dist = 20
mc.player.setPos(pos.x + dist*dire.x, pos.y + dist*dire.y, pos.z + dist*dire.z)
