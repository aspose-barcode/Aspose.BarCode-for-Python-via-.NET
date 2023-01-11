from aspose.barcode import barcoderecognition
import ExampleAssist as ta

class BarcodeReaderExamples():
    def allSupportedTypesExample(self):
        print("\n----\nallSupportedTypesExample")
        ta.set_license()
        full_path = ta.test_data_root + "code128-example-1.jpg"
        reader = barcoderecognition.BarCodeReader(full_path)
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def setQualitySettingsExample1(self):
        print("\n----\nsetQualitySettingsExample1")
        ta.set_license()
        full_path = ta.test_data_root + "code128-example-2.png"
        reader = barcoderecognition.BarCodeReader(full_path)
        reader.quality_settings = barcoderecognition.QualitySettings.high_performance
        reader.quality_settings.allow_median_smoothing = True
        reader.quality_settings.median_smoothing_window_size = 5
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def setQualitySettingsExample2(self):
        print("\n----\nsetQualitySettingsExample2")
        ta.set_license()
        full_path = ta.test_data_root + "datamatrix-example-1.png"
        reader = barcoderecognition.BarCodeReader(full_path)
        reader.quality_settings = barcoderecognition.QualitySettings.normal_quality
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def setQualitySettingsExample3(self):
            print("\n----\nsetQualitySettingsExample3")
            ta.set_license()
            full_path = ta.test_data_root + "barcodes-document-example-1.jpg"
            reader = barcoderecognition.BarCodeReader(full_path)
            reader.quality_settings = barcoderecognition.QualitySettings.high_quality
            recognized_results = reader.read_bar_codes()
            for x in recognized_results:
                print(x.code_text)
                print(x.code_type_name)

    def setQualitySettingsExample4(self):
                print("setQualitySettingsExample4")
                ta.set_license()
                full_path = ta.test_data_root + "barcodes-document-example-2.jpg"
                reader = barcoderecognition.BarCodeReader(full_path)
                reader.quality_settings = barcoderecognition.QualitySettings.high_performance
                recognized_results = reader.read_bar_codes()
                for x in recognized_results:
                    print(x.code_text)
                    print(x.code_type_name)




barcodeReaderExamples = BarcodeReaderExamples()
barcodeReaderExamples.allSupportedTypesExample()
barcodeReaderExamples.setQualitySettingsExample1()
barcodeReaderExamples.setQualitySettingsExample2()
barcodeReaderExamples.setQualitySettingsExample3()
barcodeReaderExamples.setQualitySettingsExample4()

