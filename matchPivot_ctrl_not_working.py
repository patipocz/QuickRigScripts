import maya.cmds as cmds

"""This is a script that creates controllers, groups the selected 
controler and matches group pivots to the controller pivot"""


sl = cmds.ls(sl=1)

for s in sl:
    ctrlName = s.replace("_jnt", "_ctrl")
    ctrl = cmds.circle( nr=(1, 0, 0), r=75, n=ctrlName) [0]
    group = cmds.group(ctrl, n=ctrl + "_auto")
    offset = cmds.group(group, n=ctrl + "_offset")

    ##MATCH PIVOT AUTO TO CTRL OFFSET TO AUTO
    cmds.matchTransform(ctrl, s)
    cmds.makeIdentity(ctrl, apply=True, t=1, r=1, s=1, n=0)
    cmds.matchTransform(group, s , pivots = 1)
    cmds.matchTransform(offset, s , pivots = 1)
    
    
    
    #constraining
    cmds.orientConstraint(ctrl, s, mo=0)
    #hierarchy
    #ctrl getting smaller