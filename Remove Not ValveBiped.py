import bpy
import re

def remove_not_valvebiped():
	if bpy.context.scene.objects.active.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if bpy.context.scene.objects.active.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	current_armature = bpy.data.objects[bpy.context.scene.objects.active.name]
	
	for csb in bpy.context.selected_editable_bones:
		if (re.search("^ValveBiped", csb.name) is not None):
			continue
		
		current_armature.data.edit_bones.remove(csb)

def main():
	print("--Remove Not ValveBiped (START)--")
	remove_not_valvebiped()
	print("--Remove Not ValveBiped (END)--")

main()