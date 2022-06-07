from app import app


@app.route('/test')
def test():
    return '<h1>It`s work</h1>'