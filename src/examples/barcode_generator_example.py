import inspect

import example_assist as ea

from aspose.barcode import generation
from aspose.pydrawing import Color, FontStyle


class BarcodeGeneratorExamples:
    """Examples for barcode generation using Aspose Barcode."""

    def generate_barcode_image_example1(self):
        """Generate a CODE128 barcode image (example 1) using Aspose Barcode.

        This example demonstrates basic usage of BarcodeGenerator to create a CODE128 barcode
        and save it as a PNG image to the resources directory.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        encode_type = generation.EncodeTypes.CODE128
        generator = generation.BarcodeGenerator(encode_type)
        generator.code_text = "123ABC"
        path_to_save = ea.results_root + "code128_1.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def generate_barcode_image_example2(self):
        """Generate CODABAR barcode image (example 2) using Aspose Barcode.

        This example demonstrates basic usage of BarcodeGenerator with CODABAR encoding
        and saving to a PNG file.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODABAR, "123456789")
        path_to_save = ea.results_root + "codabar.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def generate_barcode_image_example3(self):
        """Generate DATAMATRIX barcode image (example 3) using Aspose Barcode.

        This example demonstrates basic usage of BarcodeGenerator with Data Matrix encoding
        and saving to a PNG file.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        generator = generation.BarcodeGenerator(generation.EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ea.results_root + "datamatrix.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def set_barcode_type_example(self):
        """Set barcode type example.

        Demonstrates changing barcode_type property of BarcodeGenerator and saving to file.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        generator = generation.BarcodeGenerator(generation.EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ea.results_root + "barcode_type.png"
        new_type = generation.EncodeTypes.CODABAR
        generator.barcode_type = new_type
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def back_color_example(self):
        """Back color example.

        Demonstrates changing the back color of the barcode and saving to file.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        back_color = Color(0xFF, 0x00, 0x00)
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE39, "01234567")
        params = generator.parameters
        back_color_default = generator.parameters.back_color
        print("Default back color: " + hex(back_color_default.to_argb() + 2**32))
        params.back_color = back_color
        back_color_actual = generator.parameters.back_color
        print("new back color: " + hex(back_color_actual.to_argb() + 2**32))
        path_to_save = ea.results_root + "backColorExample.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def bar_color_example(self):
        """Bar color example.

        Demonstrates updating the barcode's bar color and saving to file.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        bar_color = Color(0x00, 0x00, 0xFF)
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE39, "01234567")
        bar_color_default = generator.parameters.barcode.bar_color
        print("Default bar color: " + hex(bar_color_default.to_argb() + 2**32))
        generator.parameters.barcode.bar_color = bar_color
        bar_color = generator.parameters.barcode.bar_color
        print("new bar color: " + hex(bar_color.to_argb() + 2**32))
        path_to_save = ea.results_root + "barColorExample.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def font_example(self):
        """Font customization example.

        Demonstrates adjusting caption fonts for the barcode and saving to file.
        """
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE128)
        generator.parameters.caption_above.text = "CAPTION ABOVE"
        generator.parameters.caption_above.visible = True
        generator.parameters.caption_above.font.style = FontStyle.ITALIC
        generator.parameters.caption_above.font.size.point = 5
        generator.parameters.caption_below.text = "CAPTION BELOW"
        generator.parameters.caption_below.visible = True
        generator.parameters.caption_below.font.style = FontStyle.BOLD
        generator.parameters.caption_below.font.size.pixels = 15
        generator.parameters.caption_above.font.family_name = "Verdana"
        path_to_save = ea.results_root + "fontExample.bmp"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)


barcode_generator_examples = BarcodeGeneratorExamples()
barcode_generator_examples.generate_barcode_image_example1()
barcode_generator_examples.generate_barcode_image_example2()
barcode_generator_examples.generate_barcode_image_example3()
barcode_generator_examples.set_barcode_type_example()
barcode_generator_examples.back_color_example()
barcode_generator_examples.bar_color_example()
barcode_generator_examples.font_example()
