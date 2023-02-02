import os
from eml_processing import extract_text_from_eml
import html2pdf
from PyPDF2 import PdfMerger

def text_to_pdf(text, pdf_file):
    try:
        html2pdf.HTMLToPDF(text.decode('utf-8'), pdf_file)
    except Exception as e:
        print(f"An error occurred while converting {pdf_file} to pdf: {e}")

def combine_pdfs(pdf_files, output_file):
    pdf_merger = PdfMerger()
    try:
        for pdf_file in pdf_files:
            with open(pdf_file, 'rb') as file:
                pdf_merger.append(file)
    except Exception as e:
        print("Error opening file:", e)
        return

    try:
        with open(output_file, 'wb') as file:
            pdf_merger.write(file)
    except Exception as e:
        print("Error writing file:", e)
        return

def create_pdf_folder(pdf_folder):
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

def convert_eml_to_pdf(eml_folder, pdf_folder, eml_file):
    pdf_file = os.path.join(pdf_folder, os.path.splitext(eml_file)[0] + ".pdf")
    try:
        text = extract_text_from_eml(os.path.join(eml_folder, eml_file))
        text_to_pdf(text.encode("utf-8"), pdf_file)
    except Exception as e:
        print(f"Failed to convert {eml_file} to pdf: {e}")
    return pdf_file

def combine_pdfs_func(pdf_files, output_file):
    try:
        combine_pdfs(pdf_files, output_file)
    except Exception as e:
        print(f"Failed to combine pdfs: {e}")