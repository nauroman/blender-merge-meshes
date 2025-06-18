# Blender Mesh Merger Add-on

A Blender add-on that merges all mesh objects in the scene into a single mesh object, removing all other objects in the process.

## Features

- Merges all mesh objects in your scene into one unified mesh
- Applies transforms to all objects before merging to ensure proper positioning
- Removes all non-mesh objects after merging
- Accessible through Blender's Add menu
- Includes undo support

## Installation

1. Download the `merge_meshes.py` file
2. Open Blender
3. Go to **Edit** → **Preferences** → **Add-ons**
4. Click **Install** and select the `merge_meshes.py` file
5. Enable the add-on by checking the box next to "Mesh: Mesh Merger"

## Usage

1. Create or import multiple mesh objects in your scene
2. In the 3D Viewport, press **Shift + A** to open the Add menu
3. Navigate to **Mesh** → **Merge Meshes**
4. The add-on will merge all mesh objects into a single mesh

## Requirements

- Blender 4.4.0 or higher
- At least 2 mesh objects in the scene to perform the merge operation

## How it Works

1. Identifies all mesh objects in the current scene
2. Applies location, rotation, and scale transforms to all objects
3. Joins all mesh objects into a single mesh
4. Removes all remaining objects except the merged mesh
5. Ensures the merged object is properly selected and active

## Limitations

- Requires at least 2 mesh objects to function
- All non-mesh objects in the scene will be deleted during the process
- This operation cannot be undone after saving the file

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created as a Blender add-on utility for mesh management workflows.
