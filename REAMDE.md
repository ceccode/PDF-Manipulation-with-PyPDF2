# PDF Manipulation with PyPDF2

This repository contains a Python script for manipulating PDF files using the PyPDF2 library. The script performs the following operations on a PDF file:

1. **Remove First and Last Pages**: Removes the first and last pages from a PDF.
2. **Split PDF Vertically**: Divides each page of a PDF into five equal vertical slices and saves them as separate PDF files.
3. **Split PDF into Sub-PDFs**: Divides a PDF into sub-PDFs, each containing up to five pages, and saves them as separate PDF files.

## Requirements

- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)

## Usage

1. Clone this repository or download the ZIP file.
2. Navigate to the directory containing the script and PDF files.
3. Modify the script as needed, changing the input and output file paths.
4. Open a terminal or command prompt and execute the script:

   ```
   python3 src/main.py
   ```

5. The script will perform the specified operations on the PDF files and provide feedback in the terminal.

## Script Description

### `main.py`

This script contains the functions for removing first and last pages from a PDF, splitting PDF pages vertically, and splitting a PDF into sub-PDFs.

- `remove_first_last_page(input_pdf_path, output_pdf_path)`: Removes the first and last pages of a PDF and saves the modified PDF.

- `create_folder(folder_path)`: Creates a folder if it doesn't exist.

- `split_pdf_vertically(pdf_path, output_folder)`: Splits each page of a PDF into five vertical slices and saves them as separate PDF files.

- `split_pdf(pdf_path, output_folder)`: Splits a PDF into sub-PDFs, each containing up to five pages, and saves them as separate PDF files.

## License

This project is licensed under the MIT License.