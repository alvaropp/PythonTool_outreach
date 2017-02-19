#
# Code by Matthew Mostert
#
from mine import *
import math
import time

mc = Minecraft()


def test_area_clear():
    mc.setBlocks(-59, 0, 9, -21, 76, 47, block.AIR)
    mc.setBlocks(-59, -1, 9, -21, -1, 47, block.GRASS)


def sci_to_mine_coord(x, y, z):
    """Converts Scientific Cartesian to Minecraft Cartesian Coordinates
       ----------------------------------------------------------------

    Takes in the conventional format of cartesian coordinates (x, y, z) where
    z is vertical axis and x is 0 axis, then returns the Minecraft coordinates
    where y is the vertical axis and y is 0 axis.

    Parameters
    ----------
    x : float, x position in scientific cartesian
    y : float, y position in scientific cartesian
    z : float, z position in scientific cartesian

    Returns
    -------
    x_M : float, x position in Minecraft cartesian
    y_M : float, y position in Minecraft cartesian
    z_M : float, z position in Minecraft cartesian
    """
    return y, z, x


def mine_to_sci_coord(x, y, z):
    """Converts Minecraft Cartesian to Scientific Cartesian Coordinates
       ----------------------------------------------------------------

    Takes in the Minecraft format of cartesian coordinates (x, y, z) where
    y is vertical axis and z is 0 axis, then returns the scientific coordinates
    where z is the vertical axis and x is 0 axis.

    Parameters
    ----------
    x : float, x position in Minecraft cartesian
    y : float, y position in Minecraft cartesian
    z : float, z position in Minecraft cartesian

    Returns
    -------
    x_S : float, x position in scientific cartesian
    y_S : float, y position in scientific cartesian
    z_S : float, z position in scientific cartesian
    """
    return z, x, y


def rectangularPrism(x1, y1, z1, x2, y2, z2, block):
    # input values in sci_cart form!!!!
    # converting arguments into integers
    x1 = int(round(x1))
    y1 = int(round(y1))
    z1 = int(round(z1))
    x2 = int(round(x2))
    y2 = int(round(y2))
    z2 = int(round(z2))
    # for each place, x, in range between x_min and x_max+1 (length):
    for x in range(min(x1, x2), max(x1, x2)+1):
        # for each place, y, in range between y_min and y_max+1 (height):
        for y in range(min(y1, y2), max(y1, y2)+1):
            # for each place, z, in range between z_min and z_max+1 (depth):
            for z in range(min(z1, z2), max(z1, z2)+1):
                # set block positions
                x_M, y_M, z_M = sci_to_mine_coord(x, y, z)
                mc.setBlock(x_M, y_M, z_M, block)


def build_house(l=7, h=8):
    """House Builder
       -------------

    This function takes in the position at which the player wants to build a
    procedurally generated home, and the dimensions, and builds a square house
    with suitable roofing, windows, a door, and carpeted floor.

    Parameters
    ----------
    l : int, side length of house
    h : int, height of walls of house (roof height is inferred from this)

    Returns
    -------
    NONE : constructs house in Minecraft world and prints "Home sweet home" to
    chat
    """
    mc = Minecraft()
    pos = mc.player.getTilePos()
    x, y, z = mine_to_sci_coord(pos.x, pos.y, pos.z)
    house(x, y, z, l, h)
    mc.postToChat("Home sweet home!")


def house(x1, y1, z1, l, h):
    """
    x1 : int, starting x pos
    y1 : int, starting y pos
    z1 : int, starting z pos
    rot : float, direction player is facing
    l : int, side length
    h : int, wall height
    """
    # adding offset from given position in case position is player occupied
    x1 -= int(l/2)
    y1 += 3

    # building walls and hollowing out
    rectangularPrism(x1, y1, z1, x1+l-1, y1+l-1, z1+h-1, block.COBBLESTONE)
    rectangularPrism(x1+1, y1+1, z1, x1+l-1-1, y1+l-1-1, z1+h-1, block.AIR)
    rectangularPrism(x1+int(l/2), y1, z1, x1+int(l/2), y1, z1+1, block.AIR)

    # building roof
    x_l = x1-1
    x_r = x1+l
    z_t = z1+h-2
    for i in range(h):
        if i < int(l/2)+1:
            z_t += 1
            rectangularPrism(x1-1+i, y1, z1+h-1+i, x1-1+i, y1+l-1, z1+h-1+i,
                             Block(53, 2))
            rectangularPrism(x1+l-i, y1, z1+h-1+i, x1+l-i, y1+l-1, z1+h-1+i,
                             Block(53, 3))
            if i > 1:
                rectangularPrism(x1+i-1, y1, z1+h-2+i, x1+l-i, y1, z1+h-2+i,
                             block.WOOD_PLANKS)
                rectangularPrism(x1+i-1, y1+l-1, z1+h-2+i, x1+l-i, y1+l-1,
                                 z1+h-2+i, block.WOOD_PLANKS)
            x_l += 1
            x_r -= 1
    if h <= math.ceil(l/2):
        rectangularPrism(x_l, y1, z_t, x_r,
                         y1+l-1, z_t, block.WOOD_PLANKS)
    elif l%2 != 0 and l < 2*h - 1: # if l is odd and less than double height - 1
        rectangularPrism(x1+(l/2), y1, z_t, x1+(l/2),
                         y1+l-1, z_t, block.WOOD_PLANKS)

    # adding floor
    rectangularPrism(x1, y1, z1-1, x1+l-1, y1+l-1, z1-1,
                     block.WOOL_LIGHT_GRAY)
    # adding door
    x_door, y_door, z_door = sci_to_mine_coord(x1+int(l/2), y1, z1)
    mc.setBlock(x_door, y_door, z_door, Block(64))
    mc.setBlock(x_door, y_door+1, z_door, Block(64, 8))

    # adding windows
    n_glass_z = 0
    for z in range(z1+1, z1+h-1):
        if n_glass_z < 2:
            n_glass = 0
            for y in range(y1+1, y1+l-1):
                if n_glass < 2:
                    rectangularPrism(x1, y, z, x1, y, z, block.GLASS_PANE)
                    rectangularPrism(x1+l-1, y, z, x1+l-1, y, z,
                                     block.GLASS_PANE)
                    n_glass += 1
                elif n_glass == 2:
                    n_glass += 1
                else:
                    n_glass = 0
            n_glass = 0
            for x in range(x1+1, x1+l-1):
                if n_glass < 2:
                    rectangularPrism(x, y1+l-1, z, x, y1+l-1, z,
                                     block.GLASS_PANE)
                    n_glass += 1
                elif n_glass == 2:
                    n_glass += 1
                else:
                    n_glass = 0
            if z > z1 + 4:
                n_glass = 0
                for x in range(x1+1, x1+l-1):
                    if n_glass < 2:
                        rectangularPrism(x, y1, z, x, y1, z,
                                         block.GLASS_PANE)
                        n_glass += 1
                    elif n_glass == 2:
                        n_glass += 1
                    else:
                        n_glass = 0
            if l > 5 and z < z1 + 3:
                n_glass = 0
                for x in range(x1+1, x1+l-1):
                    if x not in range(x1+int(l/2)-1, x1+int(l/2)+2):
                        if n_glass < 2:
                            rectangularPrism(x, y1, z, x, y1, z,
                                             block.GLASS_PANE)
                            n_glass += 1
                        elif n_glass == 2:
                            n_glass += 1
                        else:
                            n_glass = 0
                    else:
                        n_glass = 0
            n_glass_z += 1
        elif n_glass_z == 2:
            n_glass_z += 1
        else:
            n_glass_z = 0


if __name__ == "__main__":
    mc = Minecraft()
    pos = mc.player.getTilePos()
    test_pos = Vec3(-60, 0, 28)
    test_pos_scix, test_pos_sciy, test_pos_sciz = mine_to_sci_coord(test_pos.x,
                                                                    test_pos.y,
                                                                    test_pos.z)
    test_area_clear()
    house(test_pos_scix, test_pos_sciy, test_pos_sciz, 7, 8)
