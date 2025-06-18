bl_info = {
    "name": "Mesh Merger",
    "description": "Merge all mesh objects in the scene into a single mesh",
    "author": "Roman Naumov",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "3D Viewport > Add > Mesh > Merge Meshes",
    "warning": "",
    "wiki_url": "",
    "category": "Mesh",
}

import bpy

class MergeMeshes(bpy.types.Operator):
    """Merges all meshes into one mesh"""
    bl_idname = "mesh.merge_meshes"
    bl_label = "Merge Meshes"
    bl_description = "Merge all meshes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        # Get all mesh objects in the scene
        mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
        
        if len(mesh_objects) < 2:
            self.report({'WARNING'}, "Need at least 2 mesh objects to merge")
            return {'CANCELLED'}
        
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Apply transforms to ALL objects (including empties) before joining
        for obj in bpy.context.scene.objects:
            # Select only this object
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            # Apply all transforms to this object
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # Select all mesh objects
        for obj in mesh_objects:
            obj.select_set(True)
        
        # Set the first mesh as active object
        bpy.context.view_layer.objects.active = mesh_objects[0]
        
        # Join all selected meshes
        bpy.ops.object.join()
        
        # Get reference to the merged object (the active object after joining)
        merged_object = bpy.context.active_object

        # Apply all transforms to the merged object to prevent movement/rotation/scaling
        # when its parent or origin objects are removed
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        # Find and remove all other objects except the merged one
        objects_to_remove = []
        for obj in bpy.context.scene.objects:
            if obj != merged_object:
                objects_to_remove.append(obj)

        # Select and delete all objects except the merged one
        for obj in objects_to_remove:
            obj.select_set(True)

        # Delete selected objects
        if objects_to_remove:
            bpy.ops.object.delete()

        # Ensure only the merged object is selected
        bpy.ops.object.select_all(action='DESELECT')
        merged_object.select_set(True)
        bpy.context.view_layer.objects.active = merged_object

        self.report({'INFO'}, f"Merged {len(mesh_objects)} mesh objects")
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(MergeMeshes.bl_idname)


def register():
    bpy.utils.register_class(MergeMeshes)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(MergeMeshes)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()