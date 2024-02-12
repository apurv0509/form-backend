import os, sys 
CUR_DIR = os.getcwd()
sys.path.append(CUR_DIR)
from src.pdf_io import overlay_text_on_pdf
output_path = CUR_DIR + "/user_forms/9. ESIC Form.pdf"

from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen.canvas import Canvas
import io

class OverlayTextOnPdf:
    def __init__(self, original_pdf_path, page_index = 0):
        self.original_pdf = PdfReader(original_pdf_path)
        self.original_page = self.original_pdf.pages[page_index]
        
        self.packet = io.BytesIO()
        self.canvas = Canvas(self.packet, pagesize=(self.original_page.mediabox.width, self.original_page.mediabox.height))

    def add_text(self, text, position, font_name='Helvetica', font_size=12):
        self.canvas.setFont(font_name, font_size)
        self.canvas.drawString(position[0], position[1], text)

    def save_overlaid_pdf(self, output_pdf_path):
        self.canvas.save()
        self.packet.seek(0)
        overlaid_pdf = PdfReader(self.packet)
        overlaid_page = overlaid_pdf.pages[0]
        
        output_pdf = PdfWriter()
        overlaid_page.merge_page(self.original_page)
        output_pdf.add_page(overlaid_page)
        
        with open(output_pdf_path, "wb") as f:
            output_pdf.write(f)

def fill_form_9(pdf_path, user_data, font_size = 8, font_name="Times-Roman"):

    full_name = f"{user_data['first_name']} {user_data['middle_name']} {user_data['last_name']}".upper()
    gender = user_data["gender"].upper()
    marital_status = user_data["marital_status"].upper()
    ddmmyyyy = f"{user_data['dob_dd']}/{user_data['dob_mm']}/{user_data['dob_yyyy']}"
    doj_ddmmyyyy = f"{user_data['doj_dd']}/{user_data['doj_mm']}/{user_data['doj_yyyy']}"

    # Usage
    overlayer = OverlayTextOnPdf(pdf_path, page_index = 0)
    overlayer.add_text(full_name, (122, 740), font_name=font_name, font_size=font_size)
    overlayer.add_text(user_data['fathers_name'].upper(), (122,   713), font_name=font_name, font_size=font_size)
    overlayer.add_text(user_data['dob_dd'], (122,   635), font_name=font_name, font_size=font_size)
    overlayer.add_text(user_data['dob_mm'], (145,   635), font_name=font_name, font_size=font_size)
    overlayer.add_text(user_data['dob_yyyy'], (169,   635), font_name=font_name, font_size=font_size)
    overlayer.add_text(f"{user_data['h_addr_line1'].upper()}", (25, 610), font_name=font_name, font_size=font_size)
    overlayer.add_text(f"{user_data['h_addr_line2'].upper()} {user_data['h_addr_line3'].upper()}", (25,   600), font_name=font_name, font_size=font_size)
    overlayer.add_text(f"{user_data['h_city'].upper()}, {user_data['h_state'].upper()}", (25,   592), font_name=font_name, font_size=font_size)

    overlayer.add_text('       '.join(user_data['h_postal_code']), (60, 575), font_name=font_name, font_size=font_size)

    overlayer.add_text(f"{user_data['p_addr_line1'].upper()}", (155, 610), font_name=font_name, font_size=font_size)
    overlayer.add_text(f"{user_data['p_addr_line2'].upper()} {user_data['p_addr_line3'].upper()}", (155,   600), font_name=font_name, font_size=font_size)
    overlayer.add_text(f"{user_data['p_city'].upper()}, {user_data['p_state'].upper()}", (155,   592), font_name=font_name, font_size=font_size)

    overlayer.add_text('       '.join(user_data['p_postal_code']), (190, 575), font_name=font_name, font_size=font_size)

    overlayer.add_text(user_data['doj_dd'], (410, 715), font_name=font_name, font_size=font_size)
    overlayer.add_text(user_data['doj_mm'], (440, 715), font_name=font_name, font_size=font_size)
    overlayer.add_text(user_data['doj_yyyy'], (490, 715), font_name=font_name, font_size=font_size)

    overlayer.save_overlaid_pdf(output_path)

    return output_path
