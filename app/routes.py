'''
render_template: Used to render HTML templates (e.g., index.html, done.html).
request: Handles form data (for adding tasks).
redirect: Redirects the user to another URL after actions like adding or marking a task as done.
url_for: Dynamically generates URLs for routes.
app: The Flask app instance (imported from app/__init__.py).
db: SQLAlchemy database instance.
Task: The database model for tasks (imported from app/models.py).'''

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

# Home Page - Show pending tasks
@app.route('/') # defines the home page route (http://127.0.0.1:5000/).
def index():
    tasks = Task.query.filter_by(done=False).all()  # Get only pending tasks
    return render_template('index.html', tasks=tasks) # Renders the index.html template and passes the list of pending tasks to be displayed.

# Add New Task
@app.route('/add', methods=['POST']) # Defines the /add route, which only accepts POST requests (submitting a form).
def add_task():
    task_content = request.form.get('content') # Gets the task content entered in the form.
    if task_content:
        new_task = Task(content=task_content) # Creates new taks instance.
        db.session.add(new_task)
        db.session.commit() # Saves to the database
    return redirect(url_for('index')) # Redirect to home page after adding the task.

# Mark Task as Done
@app.route('/done/<int:task_id>') # Defines a route for marking tasks as done.
def mark_done(task_id):
    task = Task.query.get(task_id) # Fetches the enire task object(ID, content, and done status) with the given task_id from the database
    if task:  # Checks if the task exists.
        task.done = True # If taks exists, marking it as completed.
        db.session.commit() # Commit the change to database
    return redirect(url_for('index')) # Redirect to home page

# Show Completed Tasks
@app.route('/done') # Defines a route for showing completed tasks(http://127.0.0.1:5000/done).
def show_done():
    completed_tasks = Task.query.filter_by(done=True).all() #  Fetches only completed tasks (done=True) from database
    return render_template('done.html', tasks=completed_tasks) # Passes the completed tasks list to done.html for display.
