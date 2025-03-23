from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        risk = float(request.form['risk'])
        pips = float(request.form['pips'])
        if pips == 0:
            result = "Number of pips cannot be zero."
        else:
            result = risk / (pips * 10)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
