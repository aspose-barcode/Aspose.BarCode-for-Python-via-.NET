import os
import aspose.barcode

pythonLicensePath = "../resources/license/Aspose.BarCode.Python.NET.lic"
results_root = "../resources/generated/"
test_data_root = "../resources/input/"

def set_license():
    if (os.path.exists(pythonLicensePath)):
        try:
            license = aspose.barcode.License()
            license.set_license(pythonLicensePath)
        except Exception as e:
            print("Exception occurred")
            print(e)
            print("License was not installed.")
    else:
            print("Path " + pythonLicensePath + " is not correct\nLicense was not installed.")




