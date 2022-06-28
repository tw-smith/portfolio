from flask import render_template, flash, redirect
from flask_mail import Message
from app import app, mail
from app.forms import ContactForm
import logging
from datetime import datetime


logging.basicConfig(filename="logs/hp_record.log", level="WARNING")
@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    dipped = False
    form = ContactForm()

    hp_logger = logging.getLogger()
    if form.validate_on_submit():
        msg = Message("Portfolio Email", recipients=["toby2367@googlemail.com"])

        msg.body = '''Message from: {sender}.

                      Email address: {email}.

                      Message:
                      {message}'''.format(sender=form.name.data, email=form.email.data, message=form.message.data)

        if form.lastname.data:
            dipped = True
        if dipped:
            now = datetime.now()
            hp_logger.warning(now)
            hp_logger.warning('Spam email from: %s', form.email.data)
        else:
            mail.send(msg)
        #flash("Message sent successfully!")
        #return render_template('index.html',form=form)
        return redirect('/#contact')


    return render_template('index.html',form=form)
