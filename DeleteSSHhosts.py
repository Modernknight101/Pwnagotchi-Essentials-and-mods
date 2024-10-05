import os
import shutil

def delete_ssh_contents(path):
    try:
        # Check if the path exists
        if os.path.exists(path):
            # Remove all files and subdirectories in the specified path
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)  # Delete the file or symlink
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # Delete the directory
            print("Contents of the directory have been deleted.")
        else:
            print("The specified directory does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to the .ssh directory
ssh_path = r"C:\Users\17197\.ssh"
delete_ssh_contents(ssh_path)

# Prompt to exit
input("Press Enter to exit...")
