import re

import maya.cmds as cmds


def check_contiguous_range(indices):
    expected_indices = list(range(min(indices), max(indices)+1))
    return indices == expected_indices

def build_control_hierarchy(ctrl_offsets):
    """Create the controller hierarchy from a selection of group control offsets.

        ctrl_offsets: A list of groups with names that match *_<version>_ctrl_offset.
    """
    # Sort by name
    selection = sorted(ctrl_offsets)

    regex = re.compile('(?P<jointname>.+)_(?P<jointindex>\d+)_ctrl_offset')

    joint_indices = []
    joint_names = set()
    for ctrl_offset in ctrl_offsets:
        match = regex.search(ctrl_offset)
        if match:
            joint_names.add(match.group('jointname'))
            joint_indices.append(int(match.group('jointindex')))
    
    if not joint_names:
        raise ValueError("Selected groups don't match naming scheme!")

    if len(joint_names) > 1:
        raise ValueError('Selection naming scheme is not consistent! %s' % joint_names)
    joint_name = list(joint_names)[0]

    if not check_contiguous_range(joint_indices):
        raise ValueError('Selected ctrl indices are not contiguous! %s' % joint_indices)

    match = regex.search(ctrl_offsets[0])
    start_joint_index = int(match.group('jointindex'))

    for index, ctrl_offset_name in reversed(list(enumerate(selection, start=start_joint_index))):
        ctrl_index = index-1
        if ctrl_index > 0:
            ctrl_name = '%s_%03d_ctrl' % (joint_name, ctrl_index)        
            existing_parents = cmds.listRelatives(ctrl_offset_name, parent=True)
            if not existing_parents or ctrl_name not in existing_parents:
                cmds.parent(ctrl_offset_name, ctrl_name)

def build_controllers(sl):
    ctrls = []
    ctrl_offsets = []
    for s in sl:
        ctrl_name = s.replace("_jnt", "_ctrl")
        ctrl = cmds.circle( nr=(1, 0, 0), r=20, n=ctrl_name)[0]
        group = cmds.group(ctrl, n=ctrl + "_auto")
        offset = cmds.group(group, n=ctrl + "_offset")
        cmds.parentConstraint(s, offset, mo=0)
        cmds.delete(cmds.parentConstraint(s, offset))
        cmds.orientConstraint(ctrl, s, mo=0)

        ctrls.append(ctrl_name)
        ctrl_offsets.append(offset)
    return ctrls, ctrl_offsets
    


selection = cmds.ls(sl=True)
controls, control_offsets = build_controllers(selection)

build_control_hierarchy(control_offsets)

