import hou

def create_sphere():
    # Create a new geometry node
    obj = hou.node("/obj")
    geo = obj.createNode("geo", "my_geometry")

    # Create a sphere inside the geometry node
    sphere = geo.createNode("sphere", "my_sphere")

    # Set some parameters for the sphere
    sphere.parm("rad").set(2.0)
    sphere.parm("type").set(1)  # Set to "polygon sphere"

    print("Successfully created a sphere in Houdini")

# Call the function
create_sphere()

# Save the Houdini scene
hou.hipFile.save('e:/PROJECTS/houdini python integration/houdini connection test/sphere_scene.hip')
print("Saved the scene as sphere_scene.hip")