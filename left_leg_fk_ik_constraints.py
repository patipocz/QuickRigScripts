'''constrain IK to FK to RESULT JNT + (match FK to IK and Match IK to FK)'''

import maya.cmds as cmds

#left leg
resultjoints = [
"l_upperLeg_RE_jnt", 
"l_lowerLeg_RE_jnt", 
"l_ankle_RE_jnt", 
"l_ball_RE_jnt", 
"l_toes_RE_jnt",
]

fk_joints = [
"l_upperLeg_FK_jnt", 
"l_lowerLeg_FK_jnt", 
"l_ankle_FK_jnt", 
"l_ball_FK_jnt", 
"l_toes_FK_jnt",
]

ik_joints = [
"l_upperLeg_IK_jnt", 
"l_lowerLeg_IK_jnt", 
"l_ankle_IK_jnt", 
"l_ball_IK_jnt", 
"l_toes_IK_jnt",
]



for i, resultjoint in enumerate(resultjoints):
    cmds.parentConstraint(ik_joints[i], fk_joints[i], resultjoint, mo=False)