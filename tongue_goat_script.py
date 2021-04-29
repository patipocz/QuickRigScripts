'''Tongue stretch'''

tongue_joints = [
"toungue_001_jnt", 
"toungue_002_jnt", 
"toungue_003_jnt", 
"toungue_004_jnt", 
"toungue_005_jnt", 
"toungueEnd_jnt"
]

#get the length of the curve and using multiplyDivide node create stretch for IK spine by connecting the output to scale X of each IK joint
curveLength = cmds.arclen('tongue_curve', ch=True)
oldLength = cmds.getAttr('curveInfo2.al')
cmds.createNode('multiplyDivide', n='stretchNode1')
cmds.setAttr('stretchNode1.operation', 2)
cmds.setAttr('stretchNode1.i2x', oldLength)
cmds.connectAttr('curveInfo2.al', 'stretchNode1.i1x')

for jnt in tongue_joints:
    cmds.connectAttr('stretchNode1.ox', jnt + '.scaleX', f=True)
