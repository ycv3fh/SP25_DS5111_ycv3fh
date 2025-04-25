import platform
import sys

#Check  OS
def test_check_linux():
    assert platform.system() == "Linux", "Error: This script must be run on Linux."

# Check Python version
def test_python_version():
    assert sys.version_info.major == 3, "expecting major version 3"
    assert sys.version_info.minor in [12, 13], "expecting minor in 12 or 13"

