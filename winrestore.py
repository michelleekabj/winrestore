import subprocess
import sys
import ctypes
from datetime import datetime

def is_admin():
    """Check if the script is run with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_restore_point(description):
    """Create a system restore point with the given description."""
    try:
        print(f"Creating restore point: {description}...")
        subprocess.check_call(
            ["powershell", 
             "Checkpoint-Computer", 
             "-Description", f"'{description}'", 
             "-RestorePointType", "MODIFY_SETTINGS"]
        )
        print("Restore point created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create restore point. Error: {e}")

def list_restore_points():
    """List all existing system restore points."""
    try:
        print("Listing restore points...")
        result = subprocess.check_output(
            ["powershell", "Get-ComputerRestorePoint"],
            universal_newlines=True
        )
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Failed to list restore points. Error: {e}")

def main():
    if not is_admin():
        print("This script requires administrative privileges.")
        print("Please restart the script as an administrator.")
        sys.exit(1)

    print("WinRestore: Simplify System Restore Point Management")
    print("1. Create a Restore Point")
    print("2. List Restore Points")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        description = input("Enter a description for the restore point: ")
        create_restore_point(description)
    elif choice == '2':
        list_restore_points()
    elif choice == '3':
        print("Exiting WinRestore.")
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()