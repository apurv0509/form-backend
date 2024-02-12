import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf
output_path = CUR_DIR + "/user_forms/7. BGV Form- Park Hyatt.pdf"

def fill_form_7(pdf_path, user_data, font_size = 8, font_name="Times-Roman"):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['dob_dd']}/{user_data['dob_mm']}/{user_data['dob_yyyy']}"
    doj_ddmmyyyy = f"{user_data['doj_dd']}/{user_data['doj_mm']}/{user_data['doj_yyyy']}"

    overlay_text_on_pdf(pdf_path = pdf_path, 
                        text = full_name, x = 30, y = 640, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)
    
    overlay_text_on_pdf(pdf_path = output_path, 
                    text = user_data['fathers_name'].upper(), x = 30, y = 600, page_number = 1, output_path = output_path,
                    font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 330, y = 600, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['number_n_id2'], x = 150, y = 570, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['number_n_id1'], x = 250, y = 570, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = marital_status, x = 520, y = 570, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_addr_line1'].upper()}", x = 20, y = 540, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_addr_line2'].upper()} {user_data['h_addr_line3'].upper()}", x = 20, y = 530, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_city'].upper()}, {user_data['h_state'].upper()}", x = 20, y = 520, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['h_postal_code'], x = 50, y = 435, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_addr_line1'].upper()}", x = 20, y = 390, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_addr_line2'].upper()} {user_data['p_addr_line3'].upper()}", x = 20, y = 380, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_city'].upper()}, {user_data['p_state'].upper()}", x = 20, y = 370, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['p_postal_code'], x = 50, y = 300, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 80, y = 140, page_number = 1, output_path = output_path,
                        font_name=font_name, font_size=font_size)
    
    overlay_text_on_pdf(pdf_path = output_path, 
                text = user_data['designation'], x = 30, y = 680, page_number = 1, output_path = output_path,
                font_name=font_name, font_size=font_size)
    
    location = "PARK HYATT HYDERABAD"
    overlay_text_on_pdf(pdf_path = output_path, 
                    text = location, x = 370, y = 680, page_number = 1, output_path = output_path,
                    font_name=font_name, font_size=font_size)


    return output_path
