import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf
output_path = CUR_DIR + "/user_forms/2. FORM  F Nomination Gratuity Act..pdf"

def fill_form_2(pdf_path, user_data, font_size = 8, font_name="Times-Roman"):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['doj_dd']}/{user_data['doj_mm']}/{user_data['doj_yyyy']}"

    overlay_text_on_pdf(pdf_path = pdf_path, 
                    text = full_name, x = 195, y = 610, page_number = 1, output_path = output_path,
                    font_name="Times-Roman", font_size=10)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 290, y = 145, page_number = 1, output_path = output_path,
                        font_name="Times-Roman", font_size=10)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = gender, x = 290, y = 130, page_number = 1, output_path = output_path,
                        font_name="Times-Roman", font_size=10)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = marital_status, x = 290, y = 100, page_number = 1, output_path = output_path,
                        font_name="Times-Roman", font_size=10)
    
    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 290, y = 700, page_number = 2, output_path = output_path,
                        font_name="Times-Roman", font_size=10)

    return output_path
