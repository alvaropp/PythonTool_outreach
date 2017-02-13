from mine import *
import text
import fonts

def text_to_block(word, colour):
    foreground = eval("block.WOOL_{}".format(colour.upper()));
    background = block.AIR

    mc = Minecraft()
    pos = mc.player.getTilePos()
    rot = mc.player.getRotation()
    rot_p = rot + 90
    forward = text.angleToTextDirectionCardinal(rot)
    perp = text.angleToTextDirectionCardinal(rot_p)

    text.drawText(mc, fonts.FONTS['8x8'], pos - forward*20 - perp*25,
                  forward, Vec3(0,1,0), word,
                  foreground, background);

