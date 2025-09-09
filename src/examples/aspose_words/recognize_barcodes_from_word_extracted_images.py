import io
import os

import example_assist as ea

import aspose.words as aw
from aspose.barcode import barcoderecognition as barcode_recognition


def recognize_barcodes_from_word_extracted_images(word_path: str) -> list[ea.BarcodeResult]:
    print("\nRecognizeBarcodesFromWordDocumentFromExtractedImages:")

    results = []

    # Open Word document
    doc = aw.Document(word_path)

    # Iterate through all Shape nodes
    for shape in doc.get_child_nodes(aw.NodeType.SHAPE, True):
        shape = shape.as_shape()  # cast to Shape
        # Skip shapes without images
        if not shape.has_image:
            continue

        # Get image bytes
        img_bytes = shape.image_data.image_bytes
        ms = io.BytesIO(img_bytes)

        # Recognize Pdf417, QR, DataMatrix, and Aztec
        reader = barcode_recognition.BarCodeReader(
            ms,
            barcode_recognition.MultyDecodeType(
                [
                    barcode_recognition.DecodeType.PDF417,
                    barcode_recognition.DecodeType.QR,
                    barcode_recognition.DecodeType.DATA_MATRIX,
                    barcode_recognition.DecodeType.AZTEC,
                ]
            ),
        )

        for result in reader.read_bar_codes():
            barcode = ea.BarcodeResult(result.code_type_name, result.code_text)
            results.append(barcode)
            print(f"{os.path.basename(word_path)}:", barcode)

    return results


def run_example(word_file):
    assert os.path.isfile(word_file), f"Word file '{word_file}' not found"
    return recognize_barcodes_from_word_extracted_images(word_file)
