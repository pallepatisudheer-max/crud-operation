from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']

    students.append({
        'name': name,
        'age': age
    })

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    if id < len(students):
        students.pop(id)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    student = students[id]
    return render_template('edit.html', student=student, id=id)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    students[id]['name'] = request.form['name']
    students[id]['age'] = request.form['age']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)