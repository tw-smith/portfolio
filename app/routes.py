from flask import render_template
from app import app
from app.forms import ContactForm

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        pass   # submit form
    return render_template('index.html',form=form)
