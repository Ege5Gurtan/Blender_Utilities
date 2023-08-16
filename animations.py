import bpy

# Set the start and end frames for the animation
 # Change to your ending location
def add_translation_animation_to_object(object_name,initial_location,final_location,start_frame,end_frame):
    """
    Description: Add translation animation to the given object
    ###Example inputs
    object_name = "Cube"
    start_frame = 1
    end_frame = 50
    initial_location = (0, 0, 0) 
    final_location = (5, 0, 0)
    """
    
    obj = bpy.data.objects[object_name]
    # Clear existing animation data
    obj.animation_data_clear()

    # Create a new animation data
    if obj.animation_data is None:
        obj.animation_data_create()

    # Create a new action for the object
    action = bpy.data.actions.new(name="MoveAnimation")
    obj.animation_data.action = action

    # Create fcurves for X, Y, and Z location animation
    fcurve_x = action.fcurves.new(data_path="location", index=0)  # Index 0 for X-axis

    fcurve_y = action.fcurves.new(data_path="location", index=1)  # Index 1 for Y-axis

    fcurve_z = action.fcurves.new(data_path="location", index=2)  # Index 2 for Z-axis
    # Add keyframes for the initial and final locations to each fcurve
    fcurve_x.keyframe_points.insert(frame=start_frame, value=initial_location[0])
    fcurve_x.keyframe_points.insert(frame=end_frame, value=final_location[0])

    fcurve_y.keyframe_points.insert(frame=start_frame, value=initial_location[1])
    fcurve_y.keyframe_points.insert(frame=end_frame, value=final_location[1])

    fcurve_z.keyframe_points.insert(frame=start_frame, value=initial_location[2])
    fcurve_z.keyframe_points.insert(frame=end_frame, value=final_location[2])
