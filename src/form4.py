import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf

output_path = CUR_DIR + "/user_forms//4. Joining Forms.pdf"

def fill_form_4(pdf_path, user_data, font_size = 8, font_name="Times-Roman"):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['dob_dd']}/{user_data['dob_mm']}/{user_data['dob_yyyy']}"
    doj_ddmmyyyy = f"{user_data['doj_dd']}/{user_data['doj_mm']}/{user_data['doj_yyyy']}"

    overlay_text_on_pdf(pdf_path = pdf_path, 
                    text = full_name, x = 90, y = 622, page_number = 1, output_path = output_path,
                    font_name=font_name, font_size=font_size)


    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 85, y = 585, page_number = 2, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 110, y = 470, page_number = 2, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['mobile_c_code']} {user_data['mobile_number']}", x = 360, y = 470, page_number = 2, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 360, y = 450, page_number = 2, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = doj_ddmmyyyy, x = 360, y = 435, page_number = 2, output_path = output_path,
                        font_name=font_name, font_size=font_size)


    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 300, y = 675, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['fathers_name'].upper(), x = 300, y = 658, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_addr_line1'].upper()}, {user_data['h_addr_line2'].upper()}", x = 300, y = 640, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_addr_line3'].upper()} {user_data['h_city'].upper()}, {user_data['h_state'].upper()} ({user_data['h_postal_code']})", x = 300, y = 630, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 80, y = 590, page_number = 3, output_path = output_path,
                        font_name=font_name, font_size=font_size)


    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 160, y = 680, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 160, y = 640, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['city_of_birth'].upper()}, {user_data['country_of_birth'].upper()}", x = 400, y = 640, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_addr_line1'].upper()}, {user_data['p_addr_line2'].upper()}", x = 190, y = 590, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['p_addr_line3'].upper()} {user_data['p_city'].upper()}, {user_data['p_state'].upper()} ({user_data['p_postal_code']})", x = 190, y = 570, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_addr_line1'].upper()}, {user_data['h_addr_line2'].upper()}", x = 190, y = 530, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['h_addr_line3'].upper()} {user_data['h_city'].upper()}, {user_data['h_state'].upper()} ({user_data['h_postal_code']})", x = 190, y = 510, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = f"{user_data['mobile_c_code']} {user_data['mobile_number']}", x = 160, y = 480, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = user_data['email'], x = 360, y = 480, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = marital_status, x = 160, y = 390, page_number = 4, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = full_name, x = 300, y = 530, page_number = 6, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = doj_ddmmyyyy, x = 300, y = 410, page_number = 6, output_path = output_path,
                        font_name=font_name, font_size=font_size)

    overlay_text_on_pdf(pdf_path = output_path, 
                        text = ddmmyyyy, x = 300, y = 380, page_number = 6, output_path = output_path,
                        font_name=font_name, font_size=font_size)
    return output_path
