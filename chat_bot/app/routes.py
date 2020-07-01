from flask import render_template
from app import app


@app.route('/')
@app.route('/Chat Bot')
def chat_bot():
    return render_template('chat_bot.html', title='Chat Bot',
                           identity='Fabrice Jaouën',
                           github='https://github.com/Fabrice-64/OC_Project_7')