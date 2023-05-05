.\venv\Scripts\activate
$Env:FLASK_APP=".\todolist.py"
$Env:DATABASE_URL="sqlite:////todolist.db"
flask run -p 3000