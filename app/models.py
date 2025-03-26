# Imports the db object from the app module.
from app import db

''' Defines a new class called Task that represents a database model (or table)
Each instance of the Task class corresponds to a row in the database table.'''

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # This column contains primary key of each row and is typically auto-incremented.
    content = db.Column(db.String(200), nullable=False) # Column to store text data of length upto 200 characters. This field ccannot be left empty.
    done = db.Column(db.Boolean, default=False) # New task will be considered 'not done(False)' unless user specify it as 'done(True)'.

    def __repr__(self):
        return f"<Task {self.content}>"# Returns a readable string that shows the task's content.
    
'''
* __repr__ is a special method [dunder(double underscores)]in Python.
* Python automatically calls it when we print, debugging, or logging the object. 
* __repr__ is used to return a string representation of an object.
* f"" (formatted string literal) is a feature in Python that allows you to embed variables inside strings.
* self represents the current instance of the class (Task in this case).
* {self.content} is replaced with the actual value of content for that Task object.
'''