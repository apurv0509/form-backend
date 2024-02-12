import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf
output_path = CUR_DIR + "/user_forms/5. New Form 11.pdf"

def fill_form_5(pdf_path, user_data, font_size = 8, font_name='Times-Roman'):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['dob_dd']}/{user_data['dob_mm']}/{user_data['dob_yyyy']}"
    doj_ddmmyyyy = f"{user_data['doj_dd']}/{user_data['doj_mm']}/{user_data['doj_yyyy']}"

    overlay_text_on_pdf(pdf_path = pdf_path, 
                    text = full_name, x = 340, y = 685, page_number = 3, output_path = output_path,
                    font_name=font_name, font_size=10)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['fathers_name'].upper(), x = 340, y = 660, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 340, y = 638, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = gender, x = 340, y = 622, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = marital_status, x = 340, y = 610, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['email'], x = 340, y = 595, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['mobile_c_code']} {user_data['mobile_number']}", x = 340, y = 580, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = doj_ddmmyyyy, x = 340, y = 560, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['number_n_id1'], x = 340, y = 493, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['number_n_id2'], x = 340, y = 480, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    return output_path
