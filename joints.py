'''This script is creating controllers in correct hierarchy for selected jonts 
assuming they follow the naming convention of _jnt.
The user can also input the radius of the circle controller
Useful for FK setups'''

import maya.cmds as cmds


def build_controllers(selection, constraint_type = "parent", radius=10):
    '''This function creates the circle controller for all the joints in a selection, 
    checks if there is an object in the scenewith the same name
    places the controller it in the correct place using parent constraint and deleting it
    constraints the controller to the joint using the orient constraint
    it lookes at the original hierarchy of joints and replicates it in ctrl hierarchy
    '''
    parent_map = {}
    for joint in selection:
        if not '_jnt' in joint:
            raise ValueError('_jnt not in ' + joint )
        ctrl_name = joint.replace("_jnt", "_ctrl")
        
        ctrl = cmds.circle( nr=(1, 0, 0), r=radius, n=ctrl_name)[0]
        if ctrl != ctrl_name:
            raise ValueError('Duplicate ctrl ' + ctrl_name)

        group = cmds.group(ctrl, n=ctrl + "_auto")
        offset = cmds.group(group, n=ctrl + "_offset")
        cmds.parentConstraint(joint, offset, mo=0)
        cmds.delete(cmds.parentConstraint(joint, offset))
        
        if constraint_type == "parent":
            cmds.parentConstraint(ctrl, joint, mo=0)
        elif constraint_type == "orient":
            cmds.orientConstraint(ctrl, joint, mo=0)
        else:
            raise ValueError("constraint_type is unexpected value:"+ constraint_type)
            
    
        parent = cmds.listRelatives(joint, parent=True)
        if parent:
            parent = parent[0]
            parent_map[offset] =  parent.replace("_jnt", "_ctrl")
    
    for ctrl_offset, ctrl_offset_parent in parent_map.items():
        cmds.parent(ctrl_offset, ctrl_offset_parent)


def shelf_build_ctrls_hierarchy ():
    #the pop-up dialog allows for user input for the constraint type and for the radius of the circle controller, 
    #if there is no user imput the defalut radius is 10 and defalut constraint is parent
    def parent_button_push(*args):
        selection = cmds.ls(sl=True)
        radius = cmds.floatField("radiusFloatField", q=True, v=True)
        build_controllers(selection, constraint_type="parent", radius=radius)
    
    def orient_button_push(*args):
        selection = cmds.ls(sl=True)
        radius = cmds.floatField("radiusFloatField", q=True, v=True)
        build_controllers(selection, constraint_type="orient", radius=radius)
        
        
    cmds.window()
    cmds.columnLayout(adjustableColumn=True)
    
    cmds.text(label='Constraints Type')
    cmds.separator()
    cmds.button(label='Parent Constraints', command=parent_button_push)
    cmds.separator()
    cmds.button(label='Orient Constraints', command=orient_button_push)
    cmds.separator()
    cmds.rowLayout(numberOfColumns=2)
    cmds.text(label='Radius')
    cmds.floatField("radiusFloatField", value=10, minValue=0.1)
    cmds.showWindow()        
