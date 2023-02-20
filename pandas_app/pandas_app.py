import pandas as pd

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app=Flask(__name__)

df=pd.read_csv('./data/data.csv')

class Pandas(FlaskForm):
    item=StringField("element")
    submit=SubmitField("add element")

@app.route('/', methods=['GET', 'POST'])
def html_table():
    return render_template('pandas.html', tables=[df.to_html(classes='data')], 
                           titles=df.columns.values)

app.run(host='0.0.0.0', port=5000)