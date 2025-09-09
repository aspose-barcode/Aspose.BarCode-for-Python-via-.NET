import io
import os

import example_assist as ea

import aspose.pdf as apdf
from aspose.barcode import barcoderecognition as barcode_recognition
from aspose.pydrawing.imaging import ImageFormat


def recognize_barcodes_from_pdf_extracted_images(pdf_path: str) -> list[ea.BarcodeResult]:
    print("\nRecognizeBarcodesFromPDFDocumentFromExtractedImages:")

    results = []

    # Open PDF
    doc = apdf.Document(pdf_path)

    # Iterate all pages (Aspose collections are iterable in Python)
    for page_index, page in enumerate(doc.pages, start=1):
        # Create image extractor and bind to the page
        absorber = apdf.ImagePlacementAbsorber()
        page.accept(absorber)

        # Process all images on the page
        for placement in absorber.image_placements:
            # Save extracted image to an in-memory PNG stream
            buf = io.BytesIO()
            placement.save(buf, ImageFormat.png)
            buf.seek(0)

            # Recognize barcodes (PDF417, QR, DataMatrix)
            reader = barcode_recognition.BarCodeReader(
                buf,
                barcode_recognition.MultyDecodeType(
                    [
                        barcode_recognition.DecodeType.PDF417,
                        barcode_recognition.DecodeType.QR,
                        barcode_recognition.DecodeType.DATA_MATRIX,
                    ]
                ),
            )

            for result in reader.read_bar_codes():
                barcode = ea.BarcodeResult(result.code_type_name, result.code_text)
                results.append(barcode)
                print(f"{os.path.basename(pdf_path)} page {page_index}:", barcode)

    return results


def run_example(pdf_file: str):
    assert os.path.isfile(pdf_file), f"PDF file '{pdf_file}' not found"
    return recognize_barcodes_from_pdf_extracted_images(pdf_file)
