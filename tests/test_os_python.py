import platform
import sys

# Check OS
if platform.system() != "Linux":
    print("Error: This script must be run on Linux.")
    sys.exit(1)

# Check Python version
if sys.version_info.major != 3 or sys.version_info.minor not in [10, 11]:
    print(f"Error: Python version is {sys.version_info.major}.{sys.version_info.minor}. Desired versions: 3.10, 3.11.")
    sys.exit(1)

print("OS and Python version checks passed.")
