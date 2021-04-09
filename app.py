from flask import Flask,render_template,request,flash
from werkzeug.utils import redirect
from forex import convert_currency
app = Flask(__name__)
app.secret_key = "abc123"
@app.route('/')
def home_view():
    return render_template('base.html')

@app.route('/convert',methods=["POST"])
def convert_view():
    from_currency = request.form['convert_from']
    to_currency =request.form['convert_to']
    currency_amount = request.form['convert_amount']
    converted_amount= convert_currency(from_currency,to_currency,currency_amount)
    if isinstance(converted_amount,str):
        flash(converted_amount)
        return redirect("/")
    else:
        return render_template('convert.html',converted=round((converted_amount),2))
