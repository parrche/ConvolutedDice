from flask import Flask, render_template, request

from die_statistics import DieSample


app = Flask(__name__)

@app.route('/')
def home():
    # sample die roll
    die_list = (6, 6, 6)
    sample = DieSample(die_list)
    return render_template('main.html', events = sample.events, frequencies = sample.frequencies)

if __name__ == '__main__':
    app.run(debug=True)
