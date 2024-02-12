from flask import Flask, request, send_file, jsonify, make_response
from flask_cors import CORS

from docx2pdf import convert
from src.form1 import populate_docx_template
from src.form2 import fill_form_2
from src.form3 import fill_form_3
from src.form4 import fill_form_4
from src.form5 import fill_form_5
from src.form6 import fill_form_6
from src.form7 import fill_form_7
from src.form8 import fill_form_8
from src.form9 import fill_form_9

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/api/downloadForm1', methods=['POST'])
def download_form_1():
    try:
        user_data = request.json['formData']
        pdf1 = "./templates/1.-Employee-Profile.docx"
        doc = populate_docx_template(pdf1, user_data)
        temp_path = "./user_forms/Form. 1 Employee Details.docx"
        doc.save(temp_path)
        return send_file(temp_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/downloadForm2', methods=['POST'])
def download_form_2():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/2. FORM  F Nomination Gratuity Act..pdf"
        output_path = fill_form_2(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=8)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/downloadForm3', methods=['POST'])
def download_form_3():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/3. Form2 - PF.pdf"
        output_path = fill_form_3(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=8)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/downloadForm4', methods=['POST'])
def download_form_4():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/4. Joining Forms.pdf"
        output_path = fill_form_4(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=10)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/downloadForm5', methods=['POST'])
def download_form_5():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/5. New Form 11.pdf"
        output_path = fill_form_5(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=10)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/downloadForm6', methods=['POST'])
def download_form_6():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/6. Authorisation Letter for Police Verification.pdf"
        output_path = fill_form_6(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=10)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/downloadForm7', methods=['POST'])
def download_form_7():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/7. BGV Form- Park Hyatt.pdf"
        output_path = fill_form_7(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=8)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/downloadForm8', methods=['POST'])
def download_form_8():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/8. PLEDGE FOR COMMITMENT TOWARDS SAFE.pdf"
        output_path = fill_form_8(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=10)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/downloadForm9', methods=['POST'])
def download_form_9():
    try:
        user_data = request.json['formData']
        pdf2 = "./templates/9. ESIC Form.pdf"
        output_path = fill_form_9(pdf_path=pdf2, user_data=user_data, font_name="Times-Roman", font_size=6)
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5013, debug=True)
