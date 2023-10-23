from flask import render_template, flash, redirect, request
from app import app, hcaptcha
from app.forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, From, Content

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
            if hcaptcha.verify():
                to_email = To(app.config['EMAIL_ADDRESS'])
                from_email = From(app.config['EMAIL_ADDRESS'])
                subject = "Portfolio Email"
                email_body = '''Message from: {name}
                                Email address: {email}
                                Message: {message}'''.format(name=form.name.data,
                                                             email=form.email.data,
                                                             message=form.message.data)
                message = Mail(from_email, to_email, subject, plain_text_content=email_body)
                try:
                    sg = SendGridAPIClient(app.config['SENDGRID_API_KEY'])
                    response = sg.send(message)
                    flash("Success! I'll get back to you as soon as I can.")
                except Exception as e:
                    flash('Error! Message was not sent.')
                    print(e)
                return redirect('/#contact')
            else:
                flash('hCaptcha error!')
                return redirect('/#contact')
        else:
            flash('Error! Form validation failed.')
            return redirect('/#contact')

@app.route('/projects/tourtracker', methods=['GET'])
def tourtracker():
    return render_template('tourtracker.html')

@app.route('/projects/arcade', methods=['GET'])
def arcade():
    return render_template('arcade.html')

@app.route('/projects/cyclingsouth', methods=['GET'])
def cyclingsouth():
    return render_template('cyclingsouth.html')

@app.route('/projects/authserver', methods=['GET'])
def authserver():
    return render_template('authserver.html')





