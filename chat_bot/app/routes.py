from app import app

@app.route('/')
@app.route('/Chat Bot')
def chat_bot():
    return "Hello World!"