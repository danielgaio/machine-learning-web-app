from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# load the model
model = pickle.load(open('../../data/model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
