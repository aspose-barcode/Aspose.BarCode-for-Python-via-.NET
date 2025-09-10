import inspect

import example_assist as ea

from aspose.barcode import barcoderecognition as barcode_recognition


class BarcodeReaderExamples:
    """Examples demonstrating barcode reader usage."""

    def all_supported_types_example(self):
        """Recognize and print all supported barcode types from a sample image."""
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        full_path = ea.test_data_root + "code128-example-1.jpg"
        reader = barcode_recognition.BarCodeReader(full_path)
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example1(self):
        """Set high performance quality settings for Code128 barcode reading."""
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        full_path = ea.test_data_root + "code128-example-2.png"
        reader = barcode_recognition.BarCodeReader(full_path, barcode_recognition.DecodeType.CODE128)
        reader.quality_settings = barcode_recognition.QualitySettings.high_performance
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example2(self):
        """Set normal quality settings for DataMatrix barcode reading."""
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        full_path = ea.test_data_root + "datamatrix-example-1.png"
        reader = barcode_recognition.BarCodeReader(full_path, barcode_recognition.DecodeType.DATA_MATRIX)
        reader.quality_settings = barcode_recognition.QualitySettings.normal_quality
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example3(self):
        """Set high quality settings for document barcode reading."""
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        full_path = ea.test_data_root + "barcodes-document-example-1.jpg"
        reader = barcode_recognition.BarCodeReader(full_path)
        reader.quality_settings = barcode_recognition.QualitySettings.high_quality
        recognized_results = reader.read_bar_codes()
        for x in recognized_results:
            print(x.code_text)
            print(x.code_type_name)

    def set_quality_settings_example4(self):
        """Set high performance quality settings for document barcode reading."""
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        full_path = ea.test_data_root + "barcodes-document-example-2.jpg"
        reader = barcode_recognition.BarCodeReader(full_path)
        reader.quality_settings = barcode_recognition.QualitySettings.high_performance
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
