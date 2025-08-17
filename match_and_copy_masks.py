import os
import shutil

# Define directories
converted_images_dir = 'converted_images'
masks_dir = 'masks'
output_dir = 'matched_output'
output_converted_dir = os.path.join(output_dir, 'converted_images')
output_masks_dir = os.path.join(output_dir, 'masks')

# Check if the required directories exist
if not os.path.exists(converted_images_dir):
    print(f"Converted images directory '{converted_images_dir}' does not exist.")
    exit(1)

if not os.path.exists(masks_dir):
    print(f"Masks directory '{masks_dir}' does not exist.")
    exit(1)

# Create output directories
os.makedirs(output_converted_dir, exist_ok=True)
os.makedirs(output_masks_dir, exist_ok=True)

# Match and copy files
files_matched = 0
for filename in os.listdir(converted_images_dir):
    if filename.startswith('rgb') and filename.endswith('_fake_B.png'):
        # Extract the base name (e.g., 000434 from rgb_000434_fake_B.png)
        base_name = filename.split('_')[1]
        mask_filename = f"{base_name}.png"
        
        # Check if the corresponding mask exists
        mask_path = os.path.join(masks_dir, mask_filename)
        if os.path.exists(mask_path):
            # Copy the converted image
            shutil.copy(os.path.join(converted_images_dir, filename), os.path.join(output_converted_dir, filename))
            # Copy the corresponding mask
            shutil.copy(mask_path, os.path.join(output_masks_dir, mask_filename))
            files_matched += 1

if files_matched == 0:
    print("No matching files were found.")
else:
    print(f"Matched and copied {files_matched} file(s) to '{output_dir}'.")
