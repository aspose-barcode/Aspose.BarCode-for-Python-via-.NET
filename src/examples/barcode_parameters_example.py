import inspect

import example_assist as ea

from aspose.barcode import generation
from aspose.pydrawing import Color


class BarcodeParametersExample:
    def set_parameters_example(self):
        print(f"\n----\n{inspect.currentframe().f_code.co_name}")
        ea.set_license()
        new_code_text = "UPDATED_NEW"
        bar_color = Color(0x0C, 0x39, 0x25)
        assert hasattr(generation, "AutoSizeMode")
        assert hasattr(generation.AutoSizeMode, "NEAREST")
        auto_size_mode = generation.AutoSizeMode.NEAREST
        bar_code_height = 91
        bar_code_width = 133
        bar_height = 1
        barcode_gen = generation.BarcodeGenerator(generation.EncodeTypes.CODE128, "1234567891")
        assert hasattr(barcode_gen, "parameters")
        base_generation_parameters = barcode_gen.parameters
        assert hasattr(base_generation_parameters, "barcode")
        barcode_parameters = base_generation_parameters.barcode
        assert hasattr(barcode_gen, "code_text")
        barcode_gen.code_text = new_code_text
        print("code_text: " + str(barcode_gen.code_text))
        assert hasattr(barcode_parameters, "bar_color")
        barcode_parameters.bar_color = bar_color
        print("bar_color: " + hex(barcode_parameters.bar_color.to_argb() + 2**32))
        assert hasattr(base_generation_parameters, "auto_size_mode")
        base_generation_parameters.auto_size_mode = auto_size_mode
        print("auto_size_mode: " + str(base_generation_parameters.auto_size_mode))
        assert hasattr(base_generation_parameters, "image_height")
        assert hasattr(base_generation_parameters.image_height, "millimeters")
        base_generation_parameters.image_height.millimeters = bar_code_height
        print("bar_code_height: " + str(base_generation_parameters.image_height.millimeters))
        assert hasattr(base_generation_parameters, "image_width")
        assert hasattr(base_generation_parameters.image_width, "millimeters")
        base_generation_parameters.image_width.millimeters = bar_code_width
        print("bar_code_width: " + str(base_generation_parameters.image_width.millimeters))
        assert hasattr(barcode_parameters, "bar_height")
        assert hasattr(barcode_parameters.bar_height, "millimeters")
        barcode_parameters.bar_height.millimeters = bar_height
        print("bar_height: " + str(barcode_parameters.bar_height.millimeters))
        path_to_save = ea.results_root + "barcodeParametersExample.png"
        barcode_gen.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)


barcode_parameters_example = BarcodeParametersExample()
barcode_parameters_example.set_parameters_example()
