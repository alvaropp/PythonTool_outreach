import sys
sys.path.insert(0, './background')
sys.path.insert(0, './background/mcpipy/')
from text_to_blocks_code import *

#############################################
#############################################

word = "NGCM"
colour = "black"

text_to_block(word, colour)
