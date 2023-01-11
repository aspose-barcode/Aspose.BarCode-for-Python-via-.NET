from aspose.barcode import generation
from aspose.pydrawing import Color, FontStyle
import ExampleAssist as ea

class BarcodeGeneratorExamples():
    def generateBarcodeImageExample1(self):
        print("---\ngenerateBarcodeImageExample1")
        ea.set_license()
        encode_type = generation.EncodeTypes.CODE128
        generator = generation.BarcodeGenerator(encode_type)
        generator.code_text = "123ABC"
        path_to_save = ea.results_root + "code128_1.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def generateBarcodeImageExample2(self):
        print("---\ngenerateBarcodeImageExample2")
        ea.set_license()
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODABAR, "123456789")
        path_to_save = ea.results_root + "codabar.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def generateBarcodeImageExample3(self):
        print("---\ngenerateBarcodeImageExample3")
        ea.set_license()
        generator = generation.BarcodeGenerator(generation.EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ea.results_root + "datamatrix.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def setBarcodeTypeExample(self):
        print("---\nsetBarcodeTypeExample")
        ea.set_license()
        generator = generation.BarcodeGenerator(generation.EncodeTypes.DATA_MATRIX, "123456789")
        path_to_save = ea.results_root + "barcode_type.png"
        new_type = generation.EncodeTypes.CODABAR
        generator.barcode_type = new_type
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def backColorExample(self):
        print("---\nbackColorExample")
        ea.set_license()
        back_color = Color(0xFF, 0x00, 0x00)
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE_39_STANDARD, '01234567')
        params = generator.parameters
        back_color_default = generator.parameters.back_color
        print("Default back color: " + hex(back_color_default.to_argb()+2**32))
        params.back_color = back_color
        back_color_actual = generator.parameters.back_color
        print('new back color: ' + hex(back_color_actual.to_argb()+2**32))
        path_to_save = ea.results_root + "backColorExample.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def barColorExample(self):
        print("---\nbarColorExample")
        bar_color = Color(0x00, 0x00, 0xFF)
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE_39_STANDARD, '01234567')
        bar_color_default = generator.parameters.barcode.bar_color
        print("Default bar color: " + hex(bar_color_default.to_argb()+2**32))
        generator.parameters.barcode.bar_color = bar_color
        bar_color= generator.parameters.barcode.bar_color
        print('new bar color: ' + hex(bar_color.to_argb()+2**32))
        path_to_save = ea.results_root + "barColorExample.png"
        generator.save(path_to_save, generation.BarCodeImageFormat.PNG)
        print("Image was saved to " + path_to_save)

    def fontExample(self):
        print("---\nfontExample")
        generator = generation.BarcodeGenerator(generation.EncodeTypes.CODE128)
        generator.parameters.caption_above.text ="CAPTION ABOVE"
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

barcodeGeneratorExamples = BarcodeGeneratorExamples()
barcodeGeneratorExamples.generateBarcodeImageExample1()
barcodeGeneratorExamples.generateBarcodeImageExample2()
barcodeGeneratorExamples.generateBarcodeImageExample3()
barcodeGeneratorExamples.setBarcodeTypeExample()
barcodeGeneratorExamples.backColorExample()
barcodeGeneratorExamples.barColorExample()
barcodeGeneratorExamples.fontExample()
