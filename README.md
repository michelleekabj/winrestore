# WinRestore

WinRestore is a Python script designed to simplify the process of creating and managing system restore points on Windows. It provides a user-friendly interface to create restore points with custom descriptions and list all existing restore points.

## Features

- **Create Restore Points**: Easily create a system restore point by providing a custom description.
- **List Restore Points**: View all existing system restore points to keep track of your system's recovery states.

## Requirements

- Windows operating system
- Python 3.x
- Administrative privileges are required to execute this script

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/winrestore.git
   cd winrestore
   ```

2. Ensure you have Python 3.x installed on your system.

3. Run the script with administrative privileges.

## Usage

1. Open a command prompt or terminal with administrative privileges.
2. Navigate to the directory containing `winrestore.py`.
3. Execute the script:
   ```bash
   python winrestore.py
   ```

4. Follow the on-screen instructions to create or list system restore points.

## Notes

- The script requires administrative privileges to create or list system restore points. Make sure to run your command prompt or terminal as an administrator.
- The script uses PowerShell commands to interact with Windows System Restore functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.