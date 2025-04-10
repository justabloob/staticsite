import os
import shutil

def copy_files_recursive(source, destination):
    # This function copies the contents of a directory to another directory
    # check if destination exists
    if not os.path.exists(destination):
        os.mkdir(destination)
    # process each item in the source directory
    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        print(f"Copied file {src_path} to {dest_path}")
        if os.path.isfile(src_path):
            # if it's a file, copy it
            shutil.copy(src_path, dest_path)
        else:
            # if it's a directory, create it in destination and recurse
            copy_files_recursive(src_path, dest_path)