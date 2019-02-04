import bpy

def object_and_child_of_armature(obj, armature):
	if obj.type != 'MESH':
		return False
	
	if obj.parent == None:
		return False
	
	if obj.parent.name != armature.data.name:
		return False
	
	return True

def remove_bones_and_fuse_weights():
	if bpy.context.scene.objects.active.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if bpy.context.scene.objects.active.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	current_armature = bpy.data.objects[bpy.context.scene.objects.active.name]
	
	for csb in bpy.context.selected_editable_bones:
		for obj in bpy.context.scene.objects:
			if object_and_child_of_armature(obj, current_armature) == False:
				continue
			
			if csb.parent == None:
				for vg in obj.vertex_groups:
					if vg.name == csb.name:
						obj.vertex_groups.remove(vg)
						break
			else:
				vertex_group_bone = None
				vertex_group_parent = None
				
				for vg in obj.vertex_groups:
					if vg.name == csb.name:
						vertex_group_bone = vg
					elif vg.name == csb.parent.name:
						vertex_group_parent = vg
					
					if vertex_group_bone != None:
						if vertex_group_parent != None:
							break
				
				if vertex_group_bone != None:
					if vertex_group_parent == None:
						vertex_group_bone.name = csb.parent.name
					else:
						modifier = obj.modifiers.new("Fuse With Parent", type = "VERTEX_WEIGHT_MIX")
						modifier.vertex_group_a = vertex_group_parent.name
						modifier.vertex_group_b = vertex_group_bone.name
						modifier.mix_mode = 'ADD'
						modifier.mix_set = 'ALL'
		
		current_armature.data.edit_bones.remove(csb)
	
	bpy.ops.object.mode_set(mode = 'OBJECT')
	for obj in bpy.context.scene.objects:
		if object_and_child_of_armature(obj, current_armature) == False:
			continue
		
		bpy.context.scene.objects.active = obj
		
		for mod in obj.modifiers:
			if "Fuse With Parent" in mod.name:
				child_vg_name = mod.vertex_group_b
				bpy.ops.object.modifier_apply(modifier = mod.name)
				
				for vg in obj.vertex_groups:
					if vg.name == child_vg_name:
						obj.vertex_groups.remove(vg)
						break
	
	bpy.context.scene.objects.active = current_armature
	bpy.ops.object.mode_set(mode = 'EDIT')

def main():
	print("--Remove Bones And Fuse Weights (START)--")
	remove_bones_and_fuse_weights()
	print("--Remove Bones And Fuse Weights (END)--")

main()