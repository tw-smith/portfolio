from flask import render_template
from flask_mail import Message
from app import app, mail
from app.forms import ContactForm

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message("Portfolio Email", recipients=["toby2367@googlemail.com"])

        msg.body = '''Message from: {sender}.
                      Email address: {email}.
                      Message:
                      {message}'''.format(sender=form.name, email=form.email, message=form.message)
        mail.send(msg)
    return render_template('index.html',form=form)
