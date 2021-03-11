from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/<num>')
def index(num):
    return f'Hello World! {num}'

@app.route('/sup')
def sup():
    return 'Sup bro?'

if __name__ == '__main__':
    app.run(debug=True)

# Model View Controller or MVC
# Model is your database
# View is your front end
# Controller is your logic - traffic 