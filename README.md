# eml2pdf_converter Documentation

This program converts `.eml` files in a specified folder to `.pdf` files and combines them into a single `.pdf` file 
after they have been sorted into chronological order.

## Required Libraries

- os
- re
- datetime
- html2pdf
- PyPDF2
- bs4

_Note: Run pip install -r requirements.txt to install the required dependencies for the code to run._

## Files

This program consists of the following files:
- `eml2pdf_converter.py`: The main program.
- `eml_processing.py`: The functions for processing the `.eml` files.
- `pdf_tools.py`: The functions for converting the html code into pdfs.
- `requirements.txt`: The required libraries for the program.
- `README.md`: This file.


## Functions

### extract_text_from_eml(eml_file)

This function extracts the text from an `.eml` file. The text is returned as a string in `html` format.

### text_to_pdf(text, pdf_file)

This function converts the `html` string to a `.pdf` file using the `html2pdf` library.

### combine_pdfs(pdf_files, output_file)

This function combines a list of `.pdf` files into a single `.pdf` file using the `PdfMerger` library.

### extract_date(eml_file)

This function extracts the date from an `.eml` file. The date is returned as a string in the format `YYYYMMDD`.

### create_pdf_folder(pdf_folder)

This function creates a folder for storing the converted `.pdf` files if the folder does not already exist.

### rename_eml_files(eml_folder, eml_file)

This function renames an `.eml` file to include the date in the filename in the format `YYYYMMDD_<filename>.eml`.

### convert_eml_to_pdf(eml_folder, pdf_folder, eml_file)

This function converts an `.eml` file to a `.pdf` file by calling the `extract_text_from_eml` and `text_to_pdf` functions.

### combine_pdfs_func(pdf_files, output_file)

This function combines `.pdf` files into a single `.pdf` file by calling the `combine_pdfs` function.

### email2pdf()

This is the main function of the program which performs the following steps:
1. Creates the `pdf_folder` for storing the converted `.pdf` files.
2. Renames the `.eml` files in the `eml_folder` to include the date in the filename.
3. Converts the `.eml` files in the `eml_folder` to `.pdf` files.
4. Combines the converted `.pdf` files into a single `.pdf` file that is sorted chronologically.

## Usage

1. Ensure that the required libraries are installed.
2. Place the `.eml` files in the `eml_folder` (default is `./emails`).
3. Run the program using `python eml2pdf_converter.py`.
4. The combined `.pdf` file will be stored in the `pdf_folder` (default is `./pdfs`).

