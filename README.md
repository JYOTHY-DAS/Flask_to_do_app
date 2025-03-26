# 📌 Flask To-Do App

A simple To-Do web application built using Flask and SQLite. This app allows users to:

✅ Add new tasks  
✅ Mark tasks as done  
✅ View only pending tasks  
✅ View completed tasks  

## 🚀 Features
- Built with **Flask** (Python web framework)
- Uses **SQLite** as the database
- Dynamic UI with **Jinja templating**
- Basic **CSS styling** for a clean interface

---

## 📂 Folder Structure
```
/Flask_To_Do_App
│── run.py                # Runs the Flask app
│── /app                  # Application folder
│   │── __init__.py       # Initializes Flask app & DB
│   │── models.py         # Defines Task model (database)
│   │── routes.py         # Defines routes (add, mark done, show tasks)
│   │── /static           # CSS, JavaScript (optional)
│   │   └── main.css      # Styling
│   │── /templates        # HTML files
│       ├── base.html     # Base template
│       ├── index.html    # Homepage (form + task list)
│       └── done.html     # Completed tasks list
```

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Flask_To_Do_App.git
cd Flask_To_Do_App
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt  # If you have a requirements.txt
```
*(If no `requirements.txt`, manually install Flask & SQLAlchemy:)*
```bash
pip install flask flask-sqlalchemy
```

### 3️⃣ Run the Flask App
```bash
python run.py
```

### 4️⃣ Open in Browser
Go to **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** to use the app.

---

## 🖥️ Usage
- **Add a Task** → Type in the input field and click "Add Task".
- **Mark Task as Done** → Click the "✔ Done" button next to a task.
- **View Completed Tasks** → Click "Show Completed Tasks".
- **Go Back to Pending Tasks** → Click "Back to Tasks".

---

## 🔧 Future Enhancements
🔹 Add user authentication  
🔹 Implement task categories  
🔹 Improve UI with Bootstrap  

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

💡 **Contributions & Suggestions** are welcome! Feel free to fork and improve. 😊

