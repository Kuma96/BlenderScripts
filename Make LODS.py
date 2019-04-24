import bpy

def object_and_child_of_armature(obj, armature):
	if obj.type != 'MESH':
		return False
	
	if obj.parent == None:
		return False
	
	if obj.parent.name != armature.data.name:
		return False
	
	return True

def make_lods():
	if bpy.context.scene.objects.active.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if bpy.context.scene.objects.active.mode != 'OBJECT':
		print("The current mode is not object mode.")
		return
	
	#Decimation per LOD level. From LOD1 to LODn. The default amount of LODS is 5.
	#Add/Remove elements from the list to change the number of lods.
	lod_levels = [0.75, 0.50, 0.30, 0.20, 0.09]
	
	lod_levels_count = len(lod_levels)
	current_armature = bpy.data.objects[bpy.context.scene.objects.active.name]
	meshes_of_armature = []
	
	for obj in bpy.context.scene.objects:
		if object_and_child_of_armature(obj, current_armature) == False:
			continue
		meshes_of_armature.append(obj)
	
	original_meshes_count = len(meshes_of_armature)
	lods_made_count = 0
	bpy.ops.object.select_all(action = 'DESELECT')
	
	for obj in meshes_of_armature:
		original_mesh_name = obj.name
		
		i = 0
		for level in lod_levels:
			i = i + 1
			obj.select = True
			bpy.context.scene.objects.active = obj
			bpy.ops.object.duplicate()
			obj.select = False
			
			if bpy.context.scene.objects.active.data.shape_keys is not None:
				bpy.ops.object.shape_key_remove(all = True)
			
			modifier = bpy.context.scene.objects.active.modifiers.new("Make LOD", type = "DECIMATE")
			modifier.decimate_type = 'COLLAPSE'
			modifier.ratio = level
			modifier.use_collapse_triangulate = True
			modifier.use_symmetry = True
			modifier.symmetry_axis = 'X'
			
			bpy.ops.object.modifier_apply(modifier = "Make LOD")
			bpy.ops.object.mode_set(mode = 'EDIT')
			bpy.ops.mesh.select_all(action = 'SELECT')
			bpy.ops.mesh.delete_loose()
			bpy.ops.object.mode_set(mode = 'OBJECT')
			
			bpy.context.scene.objects.active.name = original_mesh_name + "_LOD" + str(i)
			bpy.context.scene.objects.active.select = False
			lods_made_count = lods_made_count + 1
	
	print("LOD Levels = " + str(lod_levels_count))
	print("Meshes used = " + str(original_meshes_count))
	print("LODS made = " + str(lods_made_count) + "/" + str(lod_levels_count*original_meshes_count))

def main():
	print("--Make LODS (START)--")
	make_lods()
	print("--Make LODS (END)--")

main()