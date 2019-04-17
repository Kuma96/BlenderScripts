import bpy
from mathutils import Vector
from math import pi

def copy_base_valvespine_rotation_male():
	current_object = bpy.context.scene.objects.active
	
	if current_object.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if current_object.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	current_object.data.edit_bones["ValveBiped.Bip01_Pelvis"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Pelvis"].head + Vector((0, 0, 0.207))
	current_object.data.edit_bones["ValveBiped.Bip01_Pelvis"].roll = pi*0/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine"].head + Vector((0, -0.20625, 0.0179))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine1"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine1"].head + Vector((0, -0.20564, 0.0239))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine1"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine2"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine2"].head + Vector((0, -0.207, 0.0032))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine2"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine4"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine4"].head + Vector((0, -0.20372, -0.0368))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine4"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Neck1"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Neck1"].head + Vector((0, 0.17323, 0.1134))
	current_object.data.edit_bones["ValveBiped.Bip01_Neck1"].roll = pi*-90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Head1"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Head1"].head + Vector((0, 0.203936, 0.0356))
	current_object.data.edit_bones["ValveBiped.Bip01_Head1"].roll = pi*-90/180
	
	current_object.data.edit_bones["ValveBiped.forward"].tail = current_object.data.edit_bones["ValveBiped.forward"].head + Vector((0.20702, 0, 0))
	current_object.data.edit_bones["ValveBiped.forward"].roll = pi*-4.1/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_R_Clavicle"].tail = current_object.data.edit_bones["ValveBiped.Bip01_R_Clavicle"].head + Vector((-0.05779, -0.01628, 0.1981))
	current_object.data.edit_bones["ValveBiped.Bip01_R_Clavicle"].roll = pi*164.058/180
	
	current_object.data.edit_bones["ValveBiped.Anim_Attachment_RH"].tail = current_object.data.edit_bones["ValveBiped.Anim_Attachment_RH"].head + Vector((-0.005, -0.20692, -0.004))
	current_object.data.edit_bones["ValveBiped.Anim_Attachment_RH"].roll = pi*55.9596/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_R_Foot"].tail = current_object.data.edit_bones["ValveBiped.Bip01_R_Foot"].head + Vector((0.00709, 0.11399, -0.17266))
	current_object.data.edit_bones["ValveBiped.Bip01_R_Foot"].roll = pi*91.4483/180

def main():
	print("--Copy Base ValveSpine Rotation Male (START)--")
	copy_base_valvespine_rotation_male()
	print("--Copy Base ValveSpine Rotation Male (END)--")

main()