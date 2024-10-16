from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

technology_data = [
    {"id": 1, "name": "Computer Science & Technology"}
]

semester_data = [
    {"id": 1, "name": "1st"},
    {"id": 2, "name": "2nd"},
    {"id": 3, "name": "3rd"},
    {"id": 4, "name": "4th"},
    {"id": 5, "name": "5th"},
    {"id": 6, "name": "6th"},
    {"id": 7, "name": "7th"}
]

session_data =[
    {"id": 4, "name": "22-23"},
    {"id": 5, "name": "23-24"},
    {"id": 6, "name": "24-25"},
    {"id": 7, "name": "25-26"}
]

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




def index():
    return render_template('index.html', teachers=teacher_data)