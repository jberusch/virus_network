# local imports
from app import app
from app.forms import LoginForm

# library imports
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login user
        return redirect(url_for('/'))
    return render_template('login.html', form=form)