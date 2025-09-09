import example_assist as ea

from aspose.barcode import barcoderecognition


class BarcodeReaderExamples:
    def all_supported_types_example(self):
        print("\n----\nallSupportedTypesExample")
        ea.set_license()
        full_path = ea.test_data_root + "code128-example-1.jpg"
        reader = barcoderecognition.BarCodeReader(full_path)
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example1(self):
        print("\n----\nsetQualitySettingsExample1")
        ea.set_license()
        full_path = ea.test_data_root + "code128-example-2.png"
        reader = barcoderecognition.BarCodeReader(full_path, barcoderecognition.DecodeType.CODE128)
        reader.quality_settings = barcoderecognition.QualitySettings.high_performance
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example2(self):
        print("\n----\nsetQualitySettingsExample2")
        ea.set_license()
        full_path = ea.test_data_root + "datamatrix-example-1.png"
        reader = barcoderecognition.BarCodeReader(full_path, barcoderecognition.DecodeType.DATA_MATRIX)
        reader.quality_settings = barcoderecognition.QualitySettings.normal_quality
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example3(self):
        print("\n----\nsetQualitySettingsExample3")
        ea.set_license()
        full_path = ea.test_data_root + "barcodes-document-example-1.jpg"
        reader = barcoderecognition.BarCodeReader(full_path)
        reader.quality_settings = barcoderecognition.QualitySettings.high_quality
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example4(self):
        print("setQualitySettingsExample4")
        ea.set_license()
        full_path = ea.test_data_root + "barcodes-document-example-2.jpg"
        reader = barcoderecognition.BarCodeReader(full_path)
        reader.quality_settings = barcoderecognition.QualitySettings.high_performance
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)


barcode_reader_examples = BarcodeReaderExamples()
barcode_reader_examples.all_supported_types_example()
barcode_reader_examples.set_quality_settings_example1()
barcode_reader_examples.set_quality_settings_example2()
barcode_reader_examples.set_quality_settings_example3()
barcode_reader_examples.set_quality_settings_example4()
