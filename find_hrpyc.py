import os

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

houdini_path = r"C:\Program Files\Side Effects Software\Houdini 20.5.278"
hrpyc_file = find_file("hrpyc.py", houdini_path)

if hrpyc_file:
    print(f"hrpyc.py found at: {hrpyc_file}")
    print(f"Directory containing hrpyc.py: {os.path.dirname(hrpyc_file)}")
else:
    print("hrpyc.py not found in the Houdini installation directory.")