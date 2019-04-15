import bpy

def object_and_child_of_armature(obj, armature):
	if obj.type != 'MESH':
		return False
	
	if obj.parent == None:
		return False
	
	if obj.parent.name != armature.data.name:
		return False
	
	return True

def delete_colors_and_sort_weights():
	if bpy.context.scene.objects.active.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if bpy.context.scene.objects.active.mode != 'OBJECT':
		print("The current mode is not object mode.")
		return
	
	current_armature = bpy.data.objects[bpy.context.scene.objects.active.name]
	organizados = 0
	
	for obj in bpy.context.scene.objects:
		if object_and_child_of_armature(obj, current_armature) == False:
			continue
		
		bpy.context.scene.objects.active = obj
		
		bpy.ops.mesh.vertex_color_remove()
		bpy.ops.object.vertex_group_remove_unused()
		bpy.ops.object.vertex_group_sort(sort_type='BONE_HIERARCHY')
		organizados = organizados + 1
	
	print(str(organizados) + " objects sorted.")

def main():
	print("--Delete Colors And Sort Weights (START)--")
	delete_colors_and_sort_weights()
	print("--Delete Colors And Sort Weights (END)--")

main()