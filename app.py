from flask import Flask, render_template, request, redirect
from db import db
from models import Student

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///s.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']

    student = Student(
        name=name,
        age=age
    )

    db.session.add(student)
    db.session.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    student = Student.query.get_or_404(id)
    return render_template('edit.html', student=student)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    student = Student.query.get_or_404(id)

    student.name = request.form['name']
    student.age = request.form['age']

    db.session.commit()

    return redirect('/')
@app.route('/database')
def database():
    students = Student.query.all()

    result = ""

    for student in students:
        result += f"ID: {student.id}, Name: {student.name}, Age: {student.age}<br>"

    return result
if __name__ == '__main__':
    app.run(debug=True)