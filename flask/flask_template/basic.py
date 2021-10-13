from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/') 
def index():
    return render_template('template.html')

@app.route('/signup_form')
def signup_form():
    return render_template('puppy.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)