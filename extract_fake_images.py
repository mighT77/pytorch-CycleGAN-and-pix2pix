import os
import shutil

# Define source and destination directories
source_dir = 'results/carla2real_gray/test_latest/images'
output_dir = 'converted_images'

# Check if the source directory exists
if not os.path.exists(source_dir):
    print(f"Source directory '{source_dir}' does not exist.")
    exit(1)

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through files in the source directory
files_copied = 0
for filename in os.listdir(source_dir):
    if filename.endswith('_fake_B.png'):
        # Construct full file paths
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(output_dir, filename)
        
        # Copy the file to the output directory
        shutil.copy(source_path, destination_path)
        files_copied += 1

if files_copied == 0:
    print("No files with '_fake_B.png' were found in the source directory.")
else:
    print(f"Copied {files_copied} file(s) with '_fake_B.png' to '{output_dir}'.")
