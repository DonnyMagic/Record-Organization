from server import app

@app.route('/')
@app.route('/index')
def index():
        return 'Server is up'