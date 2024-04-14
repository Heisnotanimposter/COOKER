import trimesh
import pyrender
import numpy as np
import matplotlib.pyplot as plt
import os

def load_and_render_3d_model(model_path, description_path=None):
    """
    Loads a 3D model, processes it for rendering, and optionally displays associated textual content.
    
    Args:
        model_path (str): The file path to the 3D model (.obj format).
        description_path (str, optional): The file path to the text file containing the description (.txt format).
    """
    # Load the 3D model
    mesh = trimesh.load(model_path, force='mesh')

    # Convert to a pyrender-compatible mesh
    mesh_pyrender = pyrender.Mesh.from_trimesh(mesh)

    # Create a pyrender scene and add the mesh
    scene = pyrender.Scene()
    scene.add(mesh_pyrender)

    # Set up the camera
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
    camera_pose = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 4.0],  # Position the camera 4 units away from the origin
        [0.0, 0.0, 0.0, 1.0]
    ])
    scene.add(camera, pose=camera_pose)

    # Set up the light similar to the camera's position
    light = pyrender.DirectionalLight(color=np.ones(3), intensity=2.0)
    scene.add(light, pose=camera_pose)

    # Render the scene
    renderer = pyrender.OffscreenRenderer(640, 480)
    color, depth = renderer.render(scene)

    # Display the rendering
    plt.figure(figsize=(10, 7.5))
    plt.subplot(1, 2, 1)
    plt.imshow(color)
    plt.axis('off')
    plt.title("3D Model Render")

    # Read and display the description if provided
    if description_path and os.path.exists(description_path):
        with open(description_path, 'r') as file:
            description = file.read()
        plt.subplot(1, 2, 2)
        plt.text(0.5, 0.5, description, fontsize=12, va='center', ha='center')
        plt.axis('off')
        plt.title("Description")
    
    plt.show()

# Usage example with placeholders for file paths
model_file_path = 'path_to_model.obj'  # Update this with your .obj file path
description_file_path = 'path_to_description.txt'  # Update this with your .txt file path

# Call the function
load_and_render_3d_model(model_file_path, description_file_path)
