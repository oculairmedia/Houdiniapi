import sys
import os

# Add Houdini Python environment to sys.path
houdini_path = r"C:\Program Files\Side Effects Software\Houdini 20.5.278"
houdini_python_path = os.path.join(houdini_path, "houdini", "python3.11libs")
sys.path.insert(0, houdini_python_path)

import hrpyc

try:
    print("Attempting to connect to Houdini RPC server...")
    connection, hou = hrpyc.import_remote_module()
    print("Successfully connected to Houdini RPC server")

    # Create a new geometry node
    obj = hou.node("/obj")
    if obj is None:
        print("Error: Could not find /obj node")
    else:
        print("Successfully found /obj node")
        geo = obj.createNode("geo", "my_geometry")
        if geo is None:
            print("Error: Could not create geometry node")
        else:
            print("Successfully created geometry node")
            
            # Create a sphere inside the geometry node
            sphere = geo.createNode("sphere", "my_sphere")
            if sphere is None:
                print("Error: Could not create sphere node")
            else:
                print("Successfully created sphere node")
                
                # Set parameters for the sphere
                for axis in ['x', 'y', 'z']:
                    rad_parm = sphere.parm(f"rad{axis}")
                    if rad_parm is None:
                        print(f"Error: Could not find 'rad{axis}' parameter")
                    else:
                        rad_parm.set(2.0)
                        print(f"Successfully set rad{axis} to 2.0")

                type_parm = sphere.parm("type")
                if type_parm is None:
                    print("Error: Could not find 'type' parameter")
                else:
                    type_parm.set(1)  # Set to "polygon sphere"
                    print("Successfully set type to polygon sphere")

            print("Attempting to save the Houdini scene...")
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