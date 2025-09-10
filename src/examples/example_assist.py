import collections
import os

import aspose.barcode

_FILE_DIR = os.path.dirname(__file__)

python_license_path = os.path.join(_FILE_DIR, "..", "resources", "license", "Aspose.BarCode.Python.NET.lic")
results_root = os.path.join(_FILE_DIR, "..", "resources", "generated") + os.sep
test_data_root = os.path.join(_FILE_DIR, "..", "resources", "input") + os.sep


def set_license():
    """Set the Aspose Barcode license if the license file exists."""
    if os.path.exists(python_license_path):
        try:
            license = aspose.barcode.License()
            license.set_license(python_license_path)
        except Exception as e:
            print("Exception occurred")
            print(e)
            print("License was not installed.")
    else:
        print("Path " + python_license_path + " is not correct\nLicense was not installed.")


# Base namedtuple for Barcode results
class BarcodeResult(collections.namedtuple("BarcodeResult", ["type_name", "data"])):
    """Container for barcode result data and its type."""

    __slots__ = ()  # no extra dict

    def __str__(self):
        """String representation of the BarcodeResult instance."""
        return f"[{self.type_name}] => '{self.data}'"
