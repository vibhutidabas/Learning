from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField,TextAreaField, TextField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__,template_folder='form_temp')

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField('what breed?', validators=[DataRequired()])
    nuetered = BooleanField("have you been nuetered?")
    mood = RadioField('pls choose your mood:',
                        choices=[('mood1','HAPPY')]  )
    food = SelectField(u'pick your food:',
                        choices=[('chi','chicken'),('b','beef')])
    feedback = TextAreaField()
    submit = SubmitField('submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['nuetered'] = form.nuetered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        
        return redirect(url_for('thank you'))

    return render_template('index.html',form=form)

@app.route('/thank you')
def thankyou():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)
