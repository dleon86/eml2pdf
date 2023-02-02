import os
import re
import email

from bs4 import BeautifulSoup
from datetime import datetime

def extract_text_from_eml(eml_file):
    try:
        with open(eml_file, 'rb') as fh:
            msg = email.message_from_bytes(fh.read())
            body = msg.get_payload(decode=True).decode('utf-8')
            soup = BeautifulSoup(body, 'html.parser')
            return soup.prettify()
            # return soup.get_text()
    except Exception as e:
        print(f"Failed to extract text from {eml_file}: {e}")
        return None

def extract_date(eml_file):
    try:
        with open(eml_file, "r") as file:
            lines = file.readlines()
            date_match = re.search(r"\s{2,}(.*)", lines[2])
            if date_match:
                date_str_split = date_match.group(1).strip().split(" ")
                date_str = " ".join(date_str_split[1:-2])
                date = datetime.strptime(date_str, "%d %b %Y %H:%M:%S")
                return date.strftime("%Y%m%d")
        return None
    except Exception as e:
        print("Error occurred while extracting date from file:", eml_file)
        print("Error:", e)
        return None

def rename_eml_files(eml_folder, eml_file):
    date = extract_date(os.path.join(eml_folder, eml_file))
    if date:
        new_filename = f"{date}_{os.path.splitext(eml_file)[0]}.eml"
        os.rename(os.path.join(eml_folder, eml_file), os.path.join(eml_folder, new_filename))