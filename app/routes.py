from flask import render_template, flash, redirect
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
                      {message}'''.format(sender=form.name.data, email=form.email.data, message=form.message.data)
        mail.send(msg)
        #flash("Message sent successfully!")
        #return render_template('index.html',form=form)
        return redirect('/#contact')


    return render_template('index.html',form=form)
