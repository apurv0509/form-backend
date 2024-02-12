from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PyPDF2 import PdfReader, PdfWriter
import io

def overlay_text_on_pdf(pdf_path, text, x, y, page_number, output_path, font_name='Helvetica', font_size=12):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.setFont(font_name, font_size)

    can.drawString(x, y, text)
    can.save()

    overlay_pdf = PdfReader(packet)
    overlay_page = overlay_pdf.pages[0]

    for i, page in enumerate(reader.pages):
        if i == page_number - 1:  # Subtract 1 to match zero-based indexing
            page.merge_page(overlay_page)
        writer.add_page(page)

    with open(output_path, 'wb') as f:
        writer.write(f)