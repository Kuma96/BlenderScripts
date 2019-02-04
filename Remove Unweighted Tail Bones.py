import bpy

def remove_unweighted_tail_bones_of_armature():
	current_object = bpy.context.scene.objects.active
	
	if current_object.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if current_object.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	root_bones = []
	
	for bone in current_object.data.edit_bones:
		if bone.parent != None:
			continue
		else:
			root_bones.append(bone)
	
	for bone in root_bones:
		remove_unweighted_tail_bones_of_chain(current_object.data, bone)

def remove_unweighted_tail_bones_of_chain(base_armature, base_bone):
	for cb in base_bone.children:
		remove_unweighted_tail_bones_of_chain(base_armature, cb)
	
	if len(base_bone.children) == 0:
		base_bone_not_used = True
		
		for obj in bpy.context.scene.objects:
			if obj.type != 'MESH':
				continue
			
			if obj.parent == None:
				continue
			
			if obj.parent.name != base_armature.name:
				continue
			
			for vg in obj.vertex_groups:
				if vg.name == base_bone.name:
					base_bone_not_used = False
					break
			
			if base_bone_not_used == False:
				break
		
		if base_bone_not_used == True:
			base_armature.edit_bones.remove(base_bone)

def main():
	print("--Remove Unweighted Tail Bones (START)--")
	remove_unweighted_tail_bones_of_armature()
	print("--Remove Unweighted Tail Bones (END)--")

main()