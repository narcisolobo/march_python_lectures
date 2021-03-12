from flask import Flask, render_template, redirect
from data import list_of_superheroes

back_end_superheroes = list_of_superheroes()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', front_end_superheroes=back_end_superheroes)

if __name__ == '__main__':
    app.run(debug=True)