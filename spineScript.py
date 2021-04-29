'''Spine Rig Script'''

import maya.cmds as cmds

#define spine result joints chain as a list

spinejoints = [
"spine_RE_001_jnt", 
"spine_RE_002_jnt", 
"spine_RE_003_jnt", 
"spine_RE_004_jnt", 
"spine_RE_005_jnt", 
"spine_RE_006_jnt", 
"spine_RE_007_jnt"
]

#orient joints
for jnt in spinejoints:
    cmds.joint(jnt, e=True, oj='xyz', secondaryAxisOrient='xup', ch=True, zso=True)
    
#duplicate the spine joints result chain to create FK joints chain
fk_joints = cmds.duplicate(spinejoints,rc=True)
for i, jnt in enumerate(fk_joints):
    fk_jnt_temp = jnt.replace('_RE_', '_FK_')
    fk_jnt = fk_jnt_temp.replace('_jnt1', '_jnt') 
    cmds.rename(jnt, fk_jnt)
    fk_joints[i] = fk_jnt
    
#duplicate the spine joints result chain to  create IK joints chain 
ik_joints = cmds.duplicate(spinejoints,rc=True)
for i, jnt in enumerate(ik_joints):
    ik_jnt_temp = jnt.replace('_RE_', '_IK_')
    ik_jnt = ik_jnt_temp.replace('_jnt1', '_jnt') 
    cmds.rename(jnt, ik_jnt)
    ik_joints[i] = ik_jnt
    
#unparent the joints in the result chain so they are all separate and children of the world
cmds.parent((spinejoints[1:7]), world=True)

#duplicate 3 joints from result chain, one on each end and one in the middle which will be controling the IK spline curve
ctrl_joints = cmds.duplicate((spinejoints[0], spinejoints[3], spinejoints[6]), rc=True)
for i, jnt in enumerate(ctrl_joints):
    ctrl_jnt_temp = jnt.replace('_RE_', '_IK_CTRL_')
    ctrl_jnt = ctrl_jnt_temp.replace('_jnt1', '_jnt') 
    cmds.rename(jnt, ctrl_jnt)
    ctrl_joints[i] = ctrl_jnt


#create an IK handle for the IK joints chain and the automaticallyconnected curve
cmds.ikHandle(name='SpineIKHandle', sj=ik_joints[0], ee=ik_joints[-1], ns=2, sol='ikSplineSolver')

#smooth bind the curve to 3 controlling joints
cmds.skinCluster('curve5',ctrl_joints)

#enable twist falloff on the IK spine
cmds.setAttr('SpineIKHandle.dTwistControlEnable', 1)
cmds.setAttr ('SpineIKHandle.dWorldUpType', 4)
cmds.setAttr('SpineIKHandle.dTwistValueType', 1)


cmds.connectAttr('spine_IK_CTRL_001_jnt.worldMatrix[0]', 'SpineIKHandle.dWorldUpMatrix', f=True)
cmds.connectAttr('spine_IK_CTRL_007_jnt.worldMatrix[0]', 'SpineIKHandle.dWorldUpMatrixEnd', f=True)

#get the length of the curve and using multiplyDivide node create stretch for IK spine by connecting the output to scale X of each IK joint
curveLength = cmds.arclen('curve5', ch=True)
oldLength = cmds.getAttr('curveInfo1.al')
cmds.createNode('multiplyDivide', n='stretchNode')
cmds.setAttr('stretchNode.operation', 2)
cmds.setAttr('stretchNode.i2x', oldLength)
cmds.connectAttr('curveInfo1.al', 'stretchNode.i1x')

for jnt in ik_joints:
    cmds.connectAttr('stretchNode.ox', jnt + '.scaleX', f=True)



#loop - old version where it parents the spine as if it was a switch between ik and fk
#index = [0, 1, 2, 3, 4, 5, 6]
#for i in index:
#    cmds.parentConstraint(ik_joints [i], fk_joints[i], spinejoints[i], mo=0)


#loop - creates a parent constraint between ik joints chain and the result chain 
#- the scaling of joints happens on IK chain but unparented joints from Result chain that the rig is skinned to are translated and inherit some transformations like twists from the IK chain
for i, spinejoint in enumerate(spinejoints):
    cmds.parentConstraint(ik_joints[i], spinejoint, mo=False)

    
    
print spinejoints    
##################

#for i, jnt in enumerate(ik_joints):
#    print i
#import riggingtools
#reload(riggingtools)
#for jnt in fk_joints:
#    print jnt
#    riggingtools.joints.build_controllers(selection, constraint_type="parent", radius=radius)

#cmds.select(fk_joints)
#riggingtools.joints.build_controllers(selection, constraint_type="orient", radius=radius)
    
    
