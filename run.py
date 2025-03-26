from app import app #Imports the app object from the app module (which refers to app/__init__.py).

if __name__ == '__main__':
    app.run(debug=True)

'''What Does __name__ == '__main__' Mean?
* In Python, every script/module has a special built-in variable called __name__.
* When you run a script directly, __name__ is set to "__main__".
* When you import a script as a module, __name__ is set to the module name instead.
* if __name__ == '__main__': checks whether the script is being run directly (not imported as a module).
* It ensures that app.run(debug=True) is executed only when you run python run.py.
'''

'''
* app.run(debug=True) Starts the Flask development server.
* The debug=True flag enables debug mode, so the app automatically reloads when you make code changes 
and displays detailed error messages in the browser if something goes wrong.
'''