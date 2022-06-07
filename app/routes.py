from flask import render_template, redirect, url_for
from app import app
from app import db
from app.models import Todo
from app.forms import AddForm


todos = []

@app.route('/')
def index():
    form = AddForm()
    counters = {'todos': 0, 'active': 0, 'complete': 0}
    todos = Todo.query.all()
    counters['todos'] = len(todos)
    return render_template('index.html', form=form, todos=todos, counters=counters)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    form = AddForm()
    if not form.validate_on_submit():
        return redirect(url_for('index'))
    #todos.append(form.body.data)
    todo = Todo(body=form.body.data)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))
