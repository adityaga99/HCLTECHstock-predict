from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('home.html')


@app.route('/predict')
def prediction():
    return render_template('prediction.html')


@app.route('/prediction', methods=['POST', 'GET'])
def predic():
    a = []
    if request.method == "POST":
        prevclose = (request.form['pclose'])
        open = (request.form['open'])
        high = (request.form['high'])
        low = (request.form['low'])
        last = (request.form['last'])
        close = (request.form['close'])
        vwap = (request.form['vwap'])
        vol = (request.form['vol'])
        trades = (request.form['trade'])
        DeliverableVolume = (request.form['del_v'])
        Deliverble = (request.form['del'])

        a.extend([prevclose, open, high, low, last, close, vwap, vol, trades, DeliverableVolume, Deliverble])

        model = joblib.load("linear_regression_model1.pkl")
        y_pred = model.predict([a])

        return render_template('prediction.html', msg="done", op=y_pred)
    return render_template("prediction.html")


if __name__ == '__main__':
    app.secret_key = "hi"
    app.run(debug=True)
