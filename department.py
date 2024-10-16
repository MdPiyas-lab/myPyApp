# department.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

fourth_semester = [
    {"id": 1, "code": "25831", "name": "Business Communication"},
    {"id": 2, "code": "26641", "name": "Java Programming"},
    {"id": 3, "code": "26642", "name": "Data Structure & Algorithm"},
    {"id": 4, "code": "26643", "name": "Computer Peripherals & Interfacing"},
    {"id": 5, "code": "26644", "name": "Web Design & Development-I"},
    {"id": 6, "code": "26841", "name": "Digital Electronics-II"},
    {"id": 7, "code": "29041", "name": "Environmental Studies"},
]

# Similarly define for fifth_semester, sixth_semester, and seventh_semester
def index():
    return render_template('index.html', subjects=fourth_semester)