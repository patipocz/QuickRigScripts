import maya.cmds as cmds

"""This is a script that groups the selected 
controler and matches grop pivots to the controller pivot"""


sl = cmds.ls(sl=1)

for s in sl:
    
    group = cmds.group(s, n=s + "_auto")
    offset = cmds.group(group, n=s + "_offset")

    ##MATCH PIVOT AUTO TO CTRL OFFSET TO AUTO
    cmds.matchTransform(group, s , pivots = 1)
    cmds.matchTransform(offset, s , pivots = 1)