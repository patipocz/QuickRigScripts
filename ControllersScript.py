import maya.cmds as cmds

sl = cmds.ls(sl=1)

for s in sl:
    ctrlName = s.replace("_jnt", "_ctrl")
    ctrl = cmds.circle( nr=(1, 0, 0), r=10, n=ctrlName) [0]
    group = cmds.group(ctrl, n=ctrl + "_auto")
    offset = cmds.group(group, n=ctrl + "_offset")
    cmds.parentConstraint(s, offset, mo=0)
    cmds.delete(cmds.parentConstraint(s, offset))
    cmds.orientConstraint(ctrl, s, mo=0)
    
