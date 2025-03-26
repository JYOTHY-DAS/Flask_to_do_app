from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

# Home Page - Show pending tasks
@app.route('/')
def index():
    tasks = Task.query.filter_by(done=False).all()  # Get only pending tasks
    return render_template('index.html', tasks=tasks)

# Add Task
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if task_content:
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

# Mark Task as Done
@app.route('/done/<int:task_id>')
def mark_done(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
    return redirect(url_for('index'))

# Show Completed Tasks
@app.route('/done')
def show_done():
    completed_tasks = Task.query.filter_by(done=True).all()
    return render_template('done.html', tasks=completed_tasks)
