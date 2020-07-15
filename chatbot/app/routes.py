from flask import render_template
from app import app


@app.route('/')
@app.route('/interface')
def interface():
    return render_template('interface.html', title='Home')
