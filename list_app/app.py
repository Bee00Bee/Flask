from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

item_list =[]

app=Flask(__name__)
app.config['SECRET_KEY']='mysecret'

item_list=['First element']

class Add_item_to_list(FlaskForm):
    item=StringField("element")
    submit=SubmitField("add element")

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'item' in request.form:
        item_list.append(request.form['item'])
    return render_template('index.html', list_be_shown=item_list,
                           add_list_element_template=Add_item_to_list())

app.run(host='0.0.0.0', port=5000)