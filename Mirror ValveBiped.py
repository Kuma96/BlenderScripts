import bpy
from math import pi

def mirror_valvebiped():
	current_object = bpy.context.scene.objects.active
	
	if current_object.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if current_object.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	bones = [
		["ValveBiped.Bip01_L_Thigh", "ValveBiped.Bip01_R_Thigh"],
		["ValveBiped.Bip01_L_Calf", "ValveBiped.Bip01_R_Calf"],
		["ValveBiped.Bip01_L_Foot", "ValveBiped.Bip01_R_Foot"],
		["ValveBiped.Bip01_L_Toe0", "ValveBiped.Bip01_R_Toe0"],
		["ValveBiped.Bip01_L_Clavicle", "ValveBiped.Bip01_R_Clavicle"],
		["ValveBiped.Bip01_L_UpperArm", "ValveBiped.Bip01_R_UpperArm"],
		["ValveBiped.Bip01_L_Forearm", "ValveBiped.Bip01_R_Forearm"],
		["ValveBiped.Bip01_L_Hand", "ValveBiped.Bip01_R_Hand"],
		["ValveBiped.Anim_Attachment_LH", "ValveBiped.Anim_Attachment_RH"],
		["ValveBiped.Bip01_L_Finger0", "ValveBiped.Bip01_R_Finger0"],
		["ValveBiped.Bip01_L_Finger01", "ValveBiped.Bip01_R_Finger01"],
		["ValveBiped.Bip01_L_Finger02", "ValveBiped.Bip01_R_Finger02"],
		["ValveBiped.Bip01_L_Finger1", "ValveBiped.Bip01_R_Finger1"],
		["ValveBiped.Bip01_L_Finger11", "ValveBiped.Bip01_R_Finger11"],
		["ValveBiped.Bip01_L_Finger12", "ValveBiped.Bip01_R_Finger12"],
		["ValveBiped.Bip01_L_Finger2", "ValveBiped.Bip01_R_Finger2"],
		["ValveBiped.Bip01_L_Finger21", "ValveBiped.Bip01_R_Finger21"],
		["ValveBiped.Bip01_L_Finger22", "ValveBiped.Bip01_R_Finger22"],
		["ValveBiped.Bip01_L_Finger3", "ValveBiped.Bip01_R_Finger3"],
		["ValveBiped.Bip01_L_Finger31", "ValveBiped.Bip01_R_Finger31"],
		["ValveBiped.Bip01_L_Finger32", "ValveBiped.Bip01_R_Finger32"],
		["ValveBiped.Bip01_L_Finger4", "ValveBiped.Bip01_R_Finger4"],
		["ValveBiped.Bip01_L_Finger41", "ValveBiped.Bip01_R_Finger41"],
		["ValveBiped.Bip01_L_Finger42", "ValveBiped.Bip01_R_Finger42"]
	]
	
	for b in bones:
		if current_object.data.edit_bones.get(b[0]) is None:
			continue
		if current_object.data.edit_bones.get(b[1]) is None:
			continue
		
		current_object.data.edit_bones[b[0]].head.x = -current_object.data.edit_bones[b[1]].head.x
		current_object.data.edit_bones[b[0]].head.y = current_object.data.edit_bones[b[1]].head.y
		current_object.data.edit_bones[b[0]].head.z = current_object.data.edit_bones[b[1]].head.z
		current_object.data.edit_bones[b[0]].tail.x = -current_object.data.edit_bones[b[1]].tail.x
		current_object.data.edit_bones[b[0]].tail.y = current_object.data.edit_bones[b[1]].tail.y
		current_object.data.edit_bones[b[0]].tail.z = current_object.data.edit_bones[b[1]].tail.z
		current_object.data.edit_bones[b[0]].roll = (pi - current_object.data.edit_bones[b[1]].roll)%(2*pi)

def main():
	print("--Mirror ValveBiped (START)--")
	mirror_valvebiped()
	print("--Mirror ValveBiped (END)--")

main()