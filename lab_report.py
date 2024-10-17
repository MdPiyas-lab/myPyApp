import os
import json
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
from student_data import student_data
from department import fourth_semester  # Import semester data
from extra_data import teacher_data

OUTPUT_DIR = 'generated_reports'

def add_text_to_pdf(input_pdf_path, output_pdf_path, text_positions):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)

    for text, position, font_size in text_positions:
        c.setFont("Times-Roman", font_size)
        c.drawString(position[0], position[1], text)

    c.save()
    packet.seek(0)

    with open(input_pdf_path, "rb") as input_pdf_file:
        existing_pdf = PyPDF2.PdfReader(input_pdf_file)
        temp_pdf = PyPDF2.PdfReader(packet)

        output = PyPDF2.PdfWriter()

        for i in range(len(existing_pdf.pages)):
            page = existing_pdf.pages[i]
            if i < len(temp_pdf.pages):
                temp_page = temp_pdf.pages[i]
                page.merge_page(temp_page)
            output.add_page(page)

        with open(output_pdf_path, "wb") as output_pdf_file:
            output.write(output_pdf_file)

def generate_lab_report_pdf(board_roll, lab_report_no, lab_report_title, date_of_submission, teacher_name, subject_name):
    output_pdf_path = f'tmp/lab_report_{lab_report_no}.pdf'
    student_info = student_data.get(board_roll)
    if not student_info:
        return None  # Student not found

    department_name = student_info["department"]
    semester = student_info["semester"]

    teacher_name = (
    f"{teacher_data[0]['name']}" 
    if isinstance(teacher_data, list) and len(teacher_data) > 0 else 'Unknown Teacher'
    )

    teacher_position = (
    f"{teacher_data[0]['position']}" 
    if isinstance(teacher_data, list) and len(teacher_data) > 0 else 'Unknown Teacher'
)


    # Assuming we want the first subject from the fourth semester
    subject_name = f"{subject_name}"

    # Define positions for text insertion (x, y coordinates)
    text_positions = [
        (str(lab_report_no), (260, 508), 20),  # Lab Report No
        (subject_name, (195, 475), 20),  # Subject Name
        (department_name, (235, 442), 20),  # Department
        (lab_report_title, (165, 410), 20),  # Title
        (teacher_name, (56, 240), 16),  # Teacher Name
        (teacher_position, (56, 220), 16),  # Teacher Position
        (date_of_submission, (205, 189), 16)  # Date of Submission
    ]

    if not os.path.exists(OUTPUT_DIR):
       os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)


    output_pdf_path = "output/lab_report_{}.pdf".format(lab_report_no) 
    add_text_to_pdf("Base.pdf", output_pdf_path, text_positions)
    return output_pdf_path  # Return only the filename part


