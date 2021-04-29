'''constrain IK to FK to RESULT JNT + (match FK to IK and Match IK to FK)'''

import maya.cmds as cmds

#right leg
resultjoints = [
"r_upperLeg_RE_jnt", 
"r_lowerLeg_RE_jnt", 
"r_ankle_RE_jnt", 
"r_ball_RE_jnt", 
"r_toes_RE_jnt",
]

fk_joints = [
"r_upperLeg_FK_jnt", 
"r_lowerLeg_FK_jnt", 
"r_ankle_FK_jnt", 
"r_ball_FK_jnt", 
"r_toes_FK_jnt",
]

ik_joints = [
"r_upperLeg_IK_jnt", 
"r_lowerLeg_IK_jnt", 
"r_ankle_IK_jnt", 
"r_ball_IK_jnt", 
"r_toes_IK_jnt",
]



for i, resultjoint in enumerate(resultjoints):
    cmds.parentConstraint(ik_joints[i], fk_joints[i], resultjoint, mo=False)