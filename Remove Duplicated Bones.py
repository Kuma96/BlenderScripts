import bpy
import re

def remove_duplicated_bones():
	if bpy.context.scene.objects.active.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if bpy.context.scene.objects.active.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	current_armature = bpy.data.objects[bpy.context.scene.objects.active.name]
	
	for csb in bpy.context.selected_editable_bones:
		if (re.search("\.001$", csb.name) is not None):
			current_armature.data.edit_bones.remove(csb)

def main():
	print("--Remove Duplicated Bones (START)--")
	remove_duplicated_bones()
	print("--Remove Duplicated Bones (END)--")

main()