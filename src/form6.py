import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf

output_path = CUR_DIR + "/user_forms/6. Authorisation Letter for Police Verification.pdf"

def fill_form_6(pdf_path, user_data, font_size = 8, font_name="Times-Roman"):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['dob_dd']}/{user_data['dob_mm']}/{user_data['dob_yyyy']}"
    doj_ddmmyyyy = f"{user_data['doj_dd']}/{user_data['doj_mm']}/{user_data['doj_yyyy']}"

    overlay_text_on_pdf(pdf_path =pdf_path, 
                    text = full_name, x = 170, y = 680, page_number = 1, output_path = output_path,
                    font_name=font_name, font_size=font_size)
    
    overlay_text_on_pdf(pdf_path = output_path, 
                text = user_data['department'], x = 375, y = 650, page_number = 1, output_path = output_path,
                font_name=font_name, font_size=font_size)


    return output_path
