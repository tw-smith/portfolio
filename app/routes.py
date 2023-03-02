from flask import render_template, flash, redirect, request
from app import app
from app.forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# TODO REMOVE for prod
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = ContactForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST':
        print('in post branch')
        print(form.validate_on_submit())
        print(form.errors)
        if form.validate_on_submit():
            message = Mail(from_email = app.config['EMAIL_ADDRESS'], 
                        to_emails = app.config['EMAIL_ADDRESS'], 
                        subject = "Portfolio Email", 
                        plain_text_content='''Message from: {sender}
                        
                                                Email address: {email}
                                            
                                                Message: {message}'''.format(sender=form.name.data, email=form.email.data, message=form.message.data))
            
            try:
                sg = SendGridAPIClient(app.config['SENDGRID_API_KEY'])
                response = sg.send(message)
                flash("Success! I'll get back to you as soon as I can.")
            except Exception as e:
                flash('Error! Message was not sent.')
            return redirect('/#contact')
        else:
            flash('Error! Form validation or reCAPTCHA failed.')
            return redirect('/#contact')





