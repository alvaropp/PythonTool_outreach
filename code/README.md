This folder will be linked to PythonTool-Mod as the scripts folder (Minecraft main menu/Mods/PythonTool).

In order to keep things simple and allow people to play around with code, simple wrapper functions with a few easy parameters are used.

To hide lengthy/tricky code, we place it in the `background` folder and import it. This way it doesn't confuse the user (hopefully) and it doesn't show up in the Computer Block's inventory.

## Challenge 1: (post to chat or print with blocks?) - `text_to_blocks.py`
Basic function: `text_to_block(word, colour)`  
  Where `word` is the desired string -ask them to change `World` to their names.  
  and `colour` is a string defining the colour, there are 16 to choose from.
