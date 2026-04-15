from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello, Docker!</h1>
        <form method="post" action="/greet">
            <input type="text" name="name" placeholder="Enter your name" />
            <input type="submit" value="Say Hello" />
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'World')
    return f"<h2>Hello, {name}!</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
