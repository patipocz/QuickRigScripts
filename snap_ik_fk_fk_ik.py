import maya.cmds as cmds
import maya.OpenMaya as om

#select joints we need
sel = cmds.ls(sl=True)

#check if right number of selections is right if itis already transformed etc

#assign selection
#fkwrist = sel[0]
#fkelbow = sel[1]
#fkshldr = sel[2]
#ikwrist = sel[3]
#ikpv = sel[4]

#assign selection
fkwrist = sel[0]
fkelbow = sel[1]
fkshldr = sel[2]
ikwrist = sel[3]
ikpv = sel[4]

#get position from fk
fkwRaw = cmds.xform(fkwrist, ws=True, q=True, t=True)
fkwPos = om.MVector(fkwRaw[0], fkwRaw[1],fkwRaw[2])

fkeRaw = cmds.xform(fkelbow, ws=True, q=True, t=True)
fkePos = om.MVector(fkeRaw[0], fkeRaw[1],fkeRaw[2])

fksRaw = cmds.xform(fkshldr, ws=True, q=True, t=True)
fksPos = om.MVector(fksRaw[0], fksRaw[1],fksRaw[2])



#set position of ik wrist ctrl
cmds.move(fkwPos.x, fkwPos.y, fkwPos.z, ikwrist)

#start figuring out pole vector position
#find the average aka midpoint between shoulder and wrist
midpoint= (fkwPos + fksPos) / 2

#find pole vector direction

pvOrigin = fkePos - midpoint

#extend that length
pvRaw = pvOrigin * 2

#positionpvRaw at midpoint
pvPos = pvRaw + midpoint

#stick pole vector at pole vector position
cmds.move(pvPos.x, pvPos.y, pvPos.z, ikpv)
