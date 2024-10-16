from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
from lab_report import generate_lab_report_pdf

app = Flask(__name__)
app.config['OUTPUT_FOLDER'] = 'output'  # Folder to store generated PDFs
app.secret_key = 'your_secret_key'  # For flashing messages 

# Teacher data
teacher_data = [
    {"id": 1, "name": "Md Noman Jahan", "position": "Instructor of (Computer) DTI"},
    {"id": 2, "name": "Bushra Sultana", "position": "Lecturer of (Accounting) DTI"},
    {"id": 3, "name": "Md. Mostafizur Rahman", "position": "Instructor of (Electrical) DTI"},
    {"id": 4, "name": "Akash Saha", "position": "Instructor of (Computer) DTI"},
    {"id": 5, "name": "Mehnaz Rashid Mim", "position": "Instructor of (Computer) DTI"},
    {"id": 6, "name": "Anayet Kabir", "position": "Lecturer of (Mathematics) DTI"},
    {"id": 7, "name": "Md. Abdul Karim", "position": "Instructor of (Computer & Telecom) DTI"},
    {"id": 8, "name": "Rabeya Akter", "position": "Sr. Lecturer of (Bangla) DTI"},
    {"id": 9, "name": "Nahid Ferdous", "position": "Lecturer of (English) DTI"},
    {"id": 10, "name": "Md. Ariful Islam", "position": "Instructor of (Textile) DTI"},
    {"id": 11, "name": "Partha Pratim Mridha", "position": "Lecturer of (Chemistry) DTI"},
    {"id": 12, "name": "Partha Mazumder", "position": "Lecturer of (Chemistry) DTI"},
    {"id": 13, "name": "Arpita Neogi", "position": "Instructor of (Architecture) DTI"},
    {"id": 14, "name": "Nawruz Imtiaz", "position": "Instructor of (Electrical) DTI"},
    {"id": 15, "name": "Israt Jahan Mim", "position": "Instructor of (Textile) DTI"},
    {"id": 16, "name": "Md. Arif Hossan", "position": "Lecturer of (English) DTI"},
    {"id": 17, "name": "Ripa Rani Sarkar", "position": "Lecturer of (Unknown) DTI"},
    {"id": 18, "name": "Md. Mamunur Rashid", "position": "Lecturer of (Mathematics) DTI"},
    {"id": 19, "name": "Khatun-E-Sumaiya", "position": "(Computer) DTI"},
    {"id": 20, "name": "Dewan Emran Mahmud Shuvo", "position": "Instructor of (Mechanical) DTI"},
    {"id": 21, "name": "Alif Laisa Roja", "position": "Instructor of (Graphics Design) DTI"},
    {"id": 22, "name": "Mizanur Rahman Morad", "position": "(Computer) DTI"},
    {"id": 23, "name": "Md. Shariful Alam", "position": "(Computer) DTI"},
    {"id": 24, "name": "Md. Abu Nayeem Khan", "position": "(Computer) DTI"}
]

# Semester data
fourth_semester = [
    {"id": 1, "code": "25831", "name": "Business Communication"},
    {"id": 2, "code": "26641", "name": "Java Programming"},
    {"id": 3, "code": "26642", "name": "Data Structure & Algorithm"},
    {"id": 4, "code": "26643", "name": "Computer Peripherals & Interfacing"},
    {"id": 5, "code": "26644", "name": "Web Design & Development-I"},
    {"id": 6, "code": "26841", "name": "Digital Electronics-II"},
    {"id": 7, "code": "29041", "name": "Environmental Studies"},
]

@app.route('/')
def index():
    return render_template('index.html', teachers=teacher_data, subjects=fourth_semester)

@app.route('/generate_report', methods=['POST'])
def generate_report():
    board_roll = request.form.get('board_roll')
    lab_report_no = request.form.get('lab_report_no')
    lab_report_title = request.form.get('lab_report_title')
    date_of_submission = request.form.get('date_of_submission')
    teacher_name = request.form.get('teacher')
    subject_name = request.form.get('subject')

    print(f"Generating PDF with: {board_roll}, {lab_report_no}, {lab_report_title}, {date_of_submission}, {teacher_name}, {subject_name}")

    # Generate the PDF
    pdf_filename = generate_lab_report_pdf(board_roll, lab_report_no, lab_report_title, date_of_submission, teacher_name, subject_name)

    if pdf_filename:  # Check if PDF was generated successfully
        return render_template('index.html', pdf_filename=os.path.basename(pdf_filename), teachers=teacher_data, subjects=fourth_semester)
    else:
        error_message = "Failed to generate the lab report PDF."
        return render_template('index.html', error_message=error_message, teachers=teacher_data, subjects=fourth_semester)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join('output', filename), as_attachment=True)

@app.route('/files')
def list_files():
    """Lists all files in the output folder."""
    files = os.listdir(app.config['OUTPUT_FOLDER'])
    return render_template('files.html', files=files)

@app.route('/download/<filename>')
def download_lab_report(filename):
    """Download a file from the output folder."""
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    flash('File not found.', 'error')
    return redirect(url_for('list_files'))

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """Delete a file from the output folder."""
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f'{filename} deleted successfully.', 'success')
    else:
        flash('File not found.', 'error')
    return redirect(url_for('list_files',host='0,0,0,0')



if __name__ == '__main__':
    app.run()
