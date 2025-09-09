import ExampleAssist as ea

from aspose.barcode import generation
from aspose.pydrawing import Color


class BarcodeParametersExample:
    def setParametersExample(self):
        print("---\nsetParametersExample")
        ea.set_license()
        newCodeText = "UPDATED_NEW"
        barColor = Color(0x0C, 0x39, 0x25)
        autoSizeMode = generation.AutoSizeMode.NEAREST
        barCodeHeight = 91
        barCodeWidth = 133
        barHeight = 1
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE128, "1234567891")
        basegenerationParameters = generator.parameters
        barcodeParameters = basegenerationParameters.barcode
        generator.code_text = newCodeText
        print("codeText: " + str(generator.code_text))
        barcodeParameters.bar_color = barColor
        print("barColor: " + hex(barcodeParameters.bar_color.to_argb() + 2**32))
        basegenerationParameters.auto_size_mode = autoSizeMode
        print("autoSizeMode: " + str(basegenerationParameters.auto_size_mode))
        basegenerationParameters.image_height.millimeters = barCodeHeight
        print("barCodeHeight: " + str(basegenerationParameters.image_height.millimeters))
        basegenerationParameters.image_width.millimeters = barCodeWidth
        print("barCodeWidth: " + str(basegenerationParameters.image_width.millimeters))
        barcodeParameters.bar_height.millimeters = barHeight
        print("barHeight: " + str(barcodeParameters.bar_height.millimeters))
        path_to_save = ea.results_root + "barcodeParametersExample.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)


barcodeParametersExample = BarcodeParametersExample()
barcodeParametersExample.setParametersExample()
