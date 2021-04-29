'''constrain IK to FK to RESULT JNT + match FK to IK and Match IK to FK'''

import maya.cmds as cmds

resultjoints = [
"r_upperArm_RE_jnt", 
"r_lowerArm_RE_jnt", 
"r_wrist_RE_jnt", 
"r_hand_RE_jnt", 
"r_fingers_001_RE_jnt", 
"r_fingers_002_RE_jnt", 
"r_fingers_003_RE_jnt", 
"r_fingersEnd_RE_jnt", 
"r_thumb_001_RE_jnt", 
"r_thumb_002_RE_jnt", 
"r_thumb_003_RE_jnt", 
"r_thumbEnd_RE_jnt"
]

fk_joints = [
"r_upperArm_FK_jnt", 
"r_lowerArm_FK_jnt", 
"r_wrist_FK_jnt", 
"r_hand_FK_jnt", 
"r_fingers_001_FK_jnt", 
"r_fingers_002_FK_jnt", 
"r_fingers_003_FK_jnt", 
"r_fingersEnd_FK_jnt", 
"r_thumb_001_FK_jnt", 
"r_thumb_002_FK_jnt", 
"r_thumb_003_FK_jnt", 
"r_thumbEnd_FK_jnt"
]
ik_joints = [
"r_upperArm_IK_jnt", 
"r_lowerArm_IK_jnt", 
"r_wrist_IK_jnt", 
"r_hand_IK_jnt", 
"r_fingers_001_IK_jnt", 
"r_fingers_002_IK_jnt", 
"r_fingers_003_IK_jnt", 
"r_fingersEnd_IK_jnt", 
"r_thumb_001_IK_jnt", 
"r_thumb_002_IK_jnt", 
"r_thumb_003_IK_jnt", 
"r_thumbEnd_IK_jnt"
]



for i, resultjoint in enumerate(resultjoints):
    cmds.parentConstraint(ik_joints[i], fk_joints[i], resultjoint, mo=False)