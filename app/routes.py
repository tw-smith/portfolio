from flask import render_template, flash, redirect
from app import app
from app.forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# TODO REMOVE for prod
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = ContactForm()

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
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        return redirect('/#contact')
    return render_template('index.html',form=form) #TODO flash some sort of error message here because form submission has not validated





