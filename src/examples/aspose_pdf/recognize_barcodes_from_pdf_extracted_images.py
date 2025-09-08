import os
import tempfile

import aspose.pdf as apdf
from aspose.barcode import barcoderecognition as barcode_recognition
import ExampleAssist as ea


def recognize_barcodes_from_pdf_extracted_images(pdf_path: str) -> None:
    print("RecognizeBarcodesFromPDFDocumentFromExtractedImages:")

    # Open PDF
    doc = apdf.Document(pdf_path)

    # Iterate all pages (Aspose collections are iterable in Python)
    for page_index, page in enumerate(doc.pages, start=1):
        # Create image extractor and bind to the page
        absorber = apdf.ImagePlacementAbsorber()
        page.accept(absorber)

        # Process all images on the page
        for placement in absorber.image_placements:
            # Save extracted image to a temporary PNG file
            tmp_path = None
            try:
                with tempfile.NamedTemporaryFile(
                    prefix=f"page{page_index}_img_",
                    suffix=".png",
                    delete=False,
                ) as tmp:
                    tmp_path = tmp.name
                    # Save the image into this file stream as PNG
                    placement.save(tmp.file)

                # Recognize (restrict to common 2D types; or use DecodeType.ALL_SUPPORTED_TYPES)
                reader = barcode_recognition.BarCodeReader(
                    tmp_path,
                    barcode_recognition.MultyDecodeType(
                        [
                            barcode_recognition.DecodeType.PDF417,
                            barcode_recognition.DecodeType.QR,
                            barcode_recognition.DecodeType.DATA_MATRIX,
                        ]
                    ),
                )

                for result in reader.read_bar_codes():
                    print(
                        f"Page {page_index}: " f"Barcode type: {result.code_type_name}, " f"data: '{result.code_text}'"
                    )

            finally:
                # Ensure temp file is removed
                if tmp_path and os.path.exists(tmp_path):
                    try:
                        os.remove(tmp_path)
                    except OSError:
                        # If cleanup fails, just continue
                        pass


def run_example():
    pdf_file = os.path.join(ea.test_data_root, "PDFDocumentWithPdf417.pdf")
    assert os.path.isfile(pdf_file), f"PDF file '{pdf_file}' not found"
    recognize_barcodes_from_pdf_extracted_images(pdf_file)
