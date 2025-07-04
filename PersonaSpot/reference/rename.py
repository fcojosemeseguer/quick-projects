import os

# Path to the directory with the images (use '.' for current directory)
folder = "./andrewtate"  # Replace with your folder name, e.g., 'images' or '.' for current directory
extension = ".png"  # Change this if your images have a different extension

files = [f for f in os.listdir(folder) if f.endswith(extension)]
files.sort()  # Sort alphabetically for consistency

for i, filename in enumerate(files, 1):
    new_name = f"img{i}{extension}"
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)
    os.rename(src, dst)

print(f"✅ Renamed {len(files)} files.")
