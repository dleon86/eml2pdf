import os

from eml_processing import rename_eml_files
from pdf_tools import create_pdf_folder, convert_eml_to_pdf, combine_pdfs_func

def email2pdf():
    eml_folder = "./emails"
    pdf_folder = "./pdfs"

    create_pdf_folder(pdf_folder)

    [rename_eml_files(eml_folder, eml_file) for eml_file in os.listdir(eml_folder) if eml_file.endswith(".eml")]

    pdf_files = [convert_eml_to_pdf(eml_folder, pdf_folder, eml_file) for eml_file in sorted(os.listdir(eml_folder)) if eml_file.endswith(".eml")]

    combine_pdfs_func(pdf_files, "./pdfs/combined_emails.pdf")


if __name__ == "__main__":

    email2pdf()

