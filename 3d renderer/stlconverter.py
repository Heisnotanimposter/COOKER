import trimesh

def prepare_for_3d_printing(input_path, output_path):
    """
    Load an OBJ file, check and repair it for 3D printing, and save as an STL file.

    Args:
        input_path (str): The path to the input OBJ file.
        output_path (str): The path where the STL file will be saved.
    """
    # Load the mesh from the OBJ file
    mesh = trimesh.load(input_path, force='mesh')

    # Check if the mesh is watertight (manifold)
    if not mesh.is_watertight:
        print("Mesh is not watertight, attempting to repair.")
        mesh = mesh.fill_holes()  # Attempt to fill holes

    # Further check and repair the mesh using built-in methods
    mesh.repair(inplace=True)

    # Optionally, simplify the mesh to reduce complexity for printing
    if mesh.faces.shape[0] > 100000:  # Arbitrary large number; adjust based on your printer's capability
        print(f"Mesh is very complex ({mesh.faces.shape[0]} faces), simplifying...")
        mesh = mesh.simplify_quadratic_decimation(100000)

    # Check for any remaining issues that could affect printing
    if not mesh.is_watertight:
        print("Unable to automatically repair the mesh to be watertight.")
    else:
        print("Mesh is ready for printing.")

    # Save the mesh as an STL file
    mesh.export(output_path, file_type='stl')
    print(f"Mesh saved as STL file to {output_path}")

# Example usage
input_obj_path = 'path_to_your_file.obj'  # Provide the actual path to your OBJ file
output_stl_path = 'path_to_output_file.stl'  # Define where to save the STL file

prepare_for_3d_printing(input_obj_path, output_stl_path)
