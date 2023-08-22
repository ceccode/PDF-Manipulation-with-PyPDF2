import os
from PyPDF2 import PdfReader, PdfWriter

def remove_first_last_page(input_pdf_path, output_pdf_path):
    pdf = PdfReader(input_pdf_path)
    num_pages = len(pdf.pages)

    if num_pages <= 2:
        print("PDF has only 2 or fewer pages. No pages removed.")
        return

    output = PdfWriter()

    for i in range(1, num_pages - 1):  # Skip the first and last pages
        page = pdf.pages[i]
        output.add_page(page)

    with open(output_pdf_path, 'wb') as output_file:
        output.write(output_file)

    print("First and last pages removed. New PDF saved:", output_pdf_path)

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def split_pdf_vertically(pdf_path, output_folder):
    pdf = PdfReader(pdf_path)
    num_pages = len(pdf.pages)
    page_width = pdf.pages[0].mediabox.width

    slice_width = page_width / 5  # Divide the page width into five equal slices

    create_folder(output_folder)  # Create the output folder

    for i, page in enumerate(pdf.pages):
        for j in range(5):
            start_x = j * slice_width
            end_x = (j + 1) * slice_width

            page.cropbox.upper_left = (start_x, 0)
            page.cropbox.upper_right = (end_x, page.mediabox.height)

            output = PdfWriter()
            output.add_page(page)

            output_path = os.path.join(
                output_folder, f'page_{i+1}_slice_{j+1}.pdf')
            with open(output_path, 'wb') as output_file:
                output.write(output_file)

def split_pdf(pdf_path, output_folder):
    pdf = PdfReader(pdf_path)
    num_pages = len(pdf.pages)

    total_sub_pdfs = num_pages // 5
    remaining_pages = num_pages % 5

    sub_pdf_count = 1
    start_page = 0

    create_folder(output_folder)  # Create the output folder

    while sub_pdf_count <= total_sub_pdfs:
        output = PdfWriter()
        for i in range(start_page, start_page + 5):
            page = pdf.pages[i]
            output.add_page(page)

        output_path = os.path.join(
            output_folder, f'sub_pdf_{sub_pdf_count}.pdf')
        with open(output_path, 'wb') as output_file:
            output.write(output_file)

        sub_pdf_count += 1
        start_page += 5

    # Handle remaining pages
    if remaining_pages > 0:
        output = PdfWriter()
        for i in range(start_page, start_page + remaining_pages):
            page = pdf.pages[i]
            output.add_page(page)

        output_path = os.path.join(
            output_folder, f'sub_pdf_{sub_pdf_count}.pdf')
        with open(output_path, 'wb') as output_file:
            output.write(output_file)


input_pdf_path = './input_data/file-to-split.pdf'
output_folder = './output_data'
output_removed_pages_path = output_folder + '/pdf-without-first-last.pdf' 

# Remove first and last pages
remove_first_last_page(input_pdf_path, output_removed_pages_path)

# Split vertically and save sub-PDFs
split_pdf_vertically(output_removed_pages_path, output_folder)
split_pdf(output_removed_pages_path, output_folder)
