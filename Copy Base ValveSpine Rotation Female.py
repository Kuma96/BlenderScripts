import bpy
from mathutils import Vector
from math import pi

def copy_base_valvespine_rotation_female():
	current_object = bpy.context.scene.objects.active
	
	if current_object.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if current_object.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	current_object.data.edit_bones["ValveBiped.Bip01_Pelvis"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Pelvis"].head + Vector((0, 0, 0.1837))
	current_object.data.edit_bones["ValveBiped.Bip01_Pelvis"].roll = pi*0/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine"].head + Vector((0, -0.183683, -0.0052))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine1"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine1"].head + Vector((0, -0.183097, 0.0155))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine1"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine2"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine2"].head + Vector((0, -0.182883, 0.0178))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine2"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Spine4"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Spine4"].head + Vector((0, -0.18344, -0.0107))
	current_object.data.edit_bones["ValveBiped.Bip01_Spine4"].roll = pi*90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Neck1"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Neck1"].head + Vector((0, 0.17647, 0.0512))
	current_object.data.edit_bones["ValveBiped.Bip01_Neck1"].roll = pi*-90/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_Head1"].tail = current_object.data.edit_bones["ValveBiped.Bip01_Head1"].head + Vector((0, 0.181018, 0.0316))
	current_object.data.edit_bones["ValveBiped.Bip01_Head1"].roll = pi*-90/180
	
	current_object.data.edit_bones["ValveBiped.forward"].tail = current_object.data.edit_bones["ValveBiped.forward"].head + Vector((0.207948, 0, 0))
	current_object.data.edit_bones["ValveBiped.forward"].roll = pi*-4.1/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_R_Clavicle"].tail = current_object.data.edit_bones["ValveBiped.Bip01_R_Clavicle"].head + Vector((-0.042665, 0.007092, 0.1786))
	current_object.data.edit_bones["ValveBiped.Bip01_R_Clavicle"].roll = pi*169.011/180
	
	current_object.data.edit_bones["ValveBiped.Anim_Attachment_RH"].tail = current_object.data.edit_bones["ValveBiped.Anim_Attachment_RH"].head + Vector((-0.0078, -0.183134, 0.0129))
	current_object.data.edit_bones["ValveBiped.Anim_Attachment_RH"].roll = pi*-97.4231/180
	
	current_object.data.edit_bones["ValveBiped.Bip01_R_Foot"].tail = current_object.data.edit_bones["ValveBiped.Bip01_R_Foot"].head + Vector((0.00533, 0.08753, -0.16148))
	current_object.data.edit_bones["ValveBiped.Bip01_R_Foot"].roll = pi*91.9222/180

def main():
	print("--Copy Base ValveSpine Rotation Female (START)--")
	copy_base_valvespine_rotation_female()
	print("--Copy Base ValveSpine Rotation Female (END)--")

main()