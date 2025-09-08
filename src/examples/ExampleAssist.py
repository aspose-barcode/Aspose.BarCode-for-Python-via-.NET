import os
import aspose.barcode

_FILE_DIR = os.path.dirname(__file__)

pythonLicensePath = os.path.join(_FILE_DIR, "..", "resources", "license", "Aspose.BarCode.Python.NET.lic")
results_root = os.path.join(_FILE_DIR, "..", "resources", "generated") + os.sep
test_data_root = os.path.join(_FILE_DIR, "..", "resources", "input") + os.sep


def set_license():
    if os.path.exists(pythonLicensePath):
        try:
            license = aspose.barcode.License()
            license.set_license(pythonLicensePath)
        except Exception as e:
            print("Exception occurred")
            print(e)
            print("License was not installed.")
    else:
        print("Path " + pythonLicensePath + " is not correct\nLicense was not installed.")
