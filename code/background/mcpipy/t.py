import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

while (1):
    time.sleep(0.2)
    try:
        entitys = mc.getPlayerEntityIds()
        for nplayer in entitys:
            try:
                print(nplayer,mc.entity.getTilePos(nplayer))
            except:
                print('no pos')
    except:
        print("err")
        