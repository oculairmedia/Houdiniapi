import sys
import os

# Add Houdini Python environment to sys.path
houdini_path = r"C:\Program Files\Side Effects Software\Houdini 20.5.278"
houdini_python_path = os.path.join(houdini_path, "houdini", "python3.11libs")
sys.path.insert(0, houdini_python_path)

import hrpyc

def print_geometry_graph(node):
    def print_node_info(node, indent=""):
        print(f"{indent}{node.name()} ({node.type().name()})")
        
        # Print parameters
        for parm in node.parms():
            print(f"{indent}  Parameter: {parm.name()} = {parm.eval()}")
        
        # Print attributes if it's a geometry node
        if node.type().category().name() == "Sop":
            geo = node.geometry()
            if geo:
                for attrib in geo.pointAttribs():
                    print(f"{indent}  Point Attribute: {attrib.name()}")
                for attrib in geo.vertexAttribs():
                    print(f"{indent}  Vertex Attribute: {attrib.name()}")
                for attrib in geo.primAttribs():
                    print(f"{indent}  Primitive Attribute: {attrib.name()}")
                for attrib in geo.globalAttribs():
                    print(f"{indent}  Global Attribute: {attrib.name()}")
        
        # Recursively print child nodes
        for child in node.children():
            print_node_info(child, indent + "  ")

    print("Geometry Graph:")
    print_node_info(node)

try:
    print("Attempting to connect to Houdini RPC server...")
    connection, hou = hrpyc.import_remote_module()
    print("Successfully connected to Houdini RPC server")

    # Create a new geometry node
    obj = hou.node("/obj")
    geo = obj.createNode("geo", "my_geometry")

    # Create a sphere inside the geometry node
    sphere = geo.createNode("sphere", "my_sphere")

    # Set some parameters for the sphere
    sphere.parm("radx").set(2.0)
    sphere.parm("rady").set(2.0)
    sphere.parm("radz").set(2.0)
    sphere.parm("type").set(1)  # Set to "polygon sphere"

    print("Successfully created a sphere in Houdini")

    # Print the geometry graph
    print_geometry_graph(geo)

    # Save the Houdini scene
    hou.hipFile.save('e:/PROJECTS/houdini python integration/houdini connection test/sphere_scene.hip')
    print("Saved the scene as sphere_scene.hip")

    # Keep the connection open until the user presses Enter
    input("Press Enter to close the connection...")

except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()

finally:
    if 'connection' in locals():
        connection.close()
        print("Connection closed")