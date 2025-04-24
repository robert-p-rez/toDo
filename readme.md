# 📝 Task Manager App

A lightweight task management web application built using **Python** and **Flask**, designed for rapid prototyping and in-memory data storage.

---

## 🚀 Features

- Add, view, and delete tasks
- In-memory task storage (no external database)
- Minimalist UI using HTML templates and CSS
- Modular architecture for easy expansion

---

## 🧰 Tech Stack

| Layer        | Technology               |
|--------------|--------------------------|
| Language     | Python 3.10+             |
| Backend      | Flask                    |
| UI Templates | Jinja2                   |
| Styling      | HTML + CSS               |
| Storage      | Python dictionary (RAM)  |
| Testing      | pytest                   |

---

## 📁 Project Structure

task_manager/ ├── app.py # App entry point, Flask initialization ├── config.py # App configuration (optional)

├── routes/ # Flask route definitions │ └── tasks.py # All task-related endpoints

├── services/ # Business logic and task handling │ └── task_service.py # Task operations (add, get, delete)

├── models/ # Data models │ └── task_model.py # Task class definition

├── templates/ # Jinja2 HTML templates │ ├── index.html │ └── task_list.html

├── static/ # CSS and static files │ └── styles.css

└── tests/ # Unit and integration tests ├── test_task_service.py └── test_routes.py


---

## ✅ Requirements

- Python 3.10+
- Flask

Install dependencies:

```bash
pip install flask

▶️ Running the App

python app.py

Open your browser to http://127.0.0.1:5000
🧪 Running Tests

pytest

📌 Notes

    Data is stored in memory and will reset when the server is restarted.

    Ideal for local use, demos, and MVPs.

📖 License

This project is licensed under the MIT License.


---

Let me know if you'd like to add badges, screenshots, or sections for deployment and contribution guidelines!

