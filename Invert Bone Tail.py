import bpy

def invert_bone_tail():
	armature = bpy.context.scene.objects.active
	
	if armature.type != 'ARMATURE':
		print("The current object is not an armature.")
		return
	
	if armature.mode != 'EDIT':
		print("The current mode is not edit mode.")
		return
	
	for csb in bpy.context.selected_editable_bones:
		dist = csb.tail - csb.head
		csb.tail = csb.head - dist

def main():
	print("--Invert Bone Tail (START)--")
	invert_bone_tail()
	print("--Invert Bone Tail (END)--")

main()