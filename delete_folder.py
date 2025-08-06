import os
import shutil

def delete_folder(folder):
    # Confirm before deletion
    confirm = input(f"Are you sure you want to delete the folder '{folder}'? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Deletion canceled.")
        return

    # Try deleting the folder
    try:
        shutil.rmtree(folder)
        print(f"Deleted folder: {folder}")
    except FileNotFoundError:
        print(f"Folder not found: {folder}")
    except PermissionError:
        print(f"Permission denied: {folder}")
    except Exception as e:
        print(f"Error deleting folder '{folder}': {e}")

    # List directory contents after deletion
    try:
        output = os.listdir('.')
        print("Directory contents:", output)
    except Exception as e:
        print(f"Error listing directory: {e}")

if __name__ == "__main__":
    folder = input("Enter the name of the folder to delete: ").strip()
    delete_folder(folder)
