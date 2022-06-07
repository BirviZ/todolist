from flask import render_template, redirect, url_for
from app import app
from app.forms import AddForm


todos = []

@app.route('/')
def index():
    form = AddForm()
    return render_template('index.html', form=form, todos=todos)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    form = AddForm()
    if not form.validate_on_submit():
        return redirect(url_for('index'))
    todos.append(form.body.data)
    return redirect(url_for('index'))
