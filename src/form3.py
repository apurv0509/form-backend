import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf
output_path = CUR_DIR + "/user_forms/3. Form2 - PF.pdf"

def fill_form_3(pdf_path, user_data, font_size = 8, font_name="Times-Roman"):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['dob_dd']}/{user_data['dob_mm']}/{user_data['dob_yyyy']}"

    overlay_text_on_pdf(pdf_path = pdf_path, 
                    text = user_data['first_name'].upper(), x = 210, y = 660, page_number = 1, output_path = output_path,
                    font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['fathers_name'].upper().split(' ')[0], x = 320, y = 660, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['middle_name']} {user_data['last_name']}".upper(), x = 420, y = 660, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 150, y = 630, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = gender, x = 185, y = 612, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = marital_status, x = 340, y = 612, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_addr_line1'].upper()}, {user_data['p_addr_line2'].upper()}", x = 210, y = 595, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_addr_line3'].upper()} {user_data['p_city'].upper()}, {user_data['p_state'].upper()} ({user_data['p_postal_code']})", x = 210, y = 580, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    return output_path
