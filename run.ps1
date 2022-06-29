.\venv\Scripts\activate
$Env:FLASK_APP=".\todolist.py"
$Env:DATABASE_URL="postgresql://birviz_dev:111@localhost/todolist"
flask run -p 3000