import bpy

def object_and_child_of_armature(obj, armature):
	if obj.type != 'MESH':
		return False
	
	if obj.parent == None:
		return False
	
	if obj.parent.name != armature.data.name:
		return False
	
	return True

def normalize_all_weights_of_all_objects():
	if bpy.context.scene.objects.active.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if bpy.context.scene.objects.active.mode != 'OBJECT':
		print("The current mode is not object mode.")
		return
	
	current_armature = bpy.data.objects[bpy.context.scene.objects.active.name]
	normalizados = 0
	
	for obj in bpy.context.scene.objects:
		if object_and_child_of_armature(obj, current_armature) == False:
			continue
		
		bpy.context.scene.objects.active = obj
		
		bpy.ops.object.vertex_group_normalize_all(group_select_mode='ALL', lock_active=False)
		bpy.ops.object.vertex_group_clean(group_select_mode='ALL')
		normalizados = normalizados + 1
	
	print("All the groups of " + str(normalizados) + " objects were normalized.")

def main():
	print("--Normalize All Weights Of All Objects (START)--")
	normalize_all_weights_of_all_objects()
	print("--Normalize All Weights Of All Objects (END)--")

main()