from flask import Flask, render_template, request
from linear_model import *

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main HTML template
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    make_model()
    # Get selected movie titles from the form
    selected_movies = request.form.getlist('selected_movies[]')

    # Now, you can send the selected movies to your program and run the prediction function
    winner = run_prediction(selected_movies)

    # Render the result HTML template
    return render_template('result.html', winner=winner)

def run_prediction(selected_movies):
    print(f"Selected movies: {selected_movies}")
    predict_winner(selected_movies)
    return "Predicted Winner"

if __name__ == '__main__':
    app.run(debug=True)
