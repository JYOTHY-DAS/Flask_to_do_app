from app import app #Imports the app object from the app module (i.e app.py)

if __name__ == '__main__': #Ensures that the script runs only when executed directly (python run.py). This block won't run in another module.
    app.run(debug=True) #Starts the Flask development server.


'''
The debug=True flag:

*) Enables debug mode, allowing automatic reloading on changes.

*) Displays detailed error messages in the browser if the app crashes.'''