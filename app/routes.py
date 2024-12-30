from flask import flash, redirect, render_template, request
from requests import post
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, From, Mail, To

from app import app
from app.forms import ContactForm


def validate_hcaptcha(client_response):
    payload = {"response": client_response, "secret": app.config["HCAPTCHA_SECRET_KEY"]}
    response = post(app.config["HCAPTCHA_VERIFY_URL"], data=payload)
    return response.json()["success"]


@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    form = ContactForm()
    if request.method == "GET":
        return render_template("index.html", form=form)
    elif request.method == "POST":
        print("in post branch")
        print(form.validate_on_submit())
        print(form.errors)
        if form.validate_on_submit():
            if not validate_hcaptcha(request.form["h-captcha-response"]):
                flash("Captcha error!")
                return redirect("/#contact")
            to_email = To(app.config["EMAIL_ADDRESS"])
            from_email = From(app.config["EMAIL_ADDRESS"])
            subject = "Portfolio Email"
            email_body = """Message from: {name}
                            Email address: {email}
                            Message: {message}""".format(
                name=form.name.data, email=form.email.data, message=form.message.data
            )
            message = Mail(from_email, to_email, subject, plain_text_content=email_body)
            try:
                sg = SendGridAPIClient(app.config["SENDGRID_API_KEY"])
                response = sg.send(message)
                flash("Success! I'll get back to you as soon as I can.")
            except Exception as e:
                flash("Error! Message was not sent.")
                print(e)
            return redirect("/#contact")
        else:
            flash("Error! Form validation failed.")
            return redirect("/#contact")


@app.route("/projects/tourtracker.html", methods=["GET"])
def tourtracker():
    return render_template(
        "tourtracker_template.html",
        project_title="Tour Tracker",
        project_image_url="../static/tourtracker_home_screely.png",
        project_website={
            "url": "https://tourtracker.tw-smith.me",
            "desc": "tourtracker.tw-smith.me",
        },
        project_repo=[
            {
                "url": "https://github.com/tw-smith/tourtracker",
                "desc": "github.com/tw-smith/tourtracker",
            }
        ],
    )


@app.route("/projects/arcade.html", methods=["GET"])
def arcade():
    return render_template(
        "arcade_template.html",
        project_title="Arcade",
        project_image_url="../static/arcade_home_screely.png",
        project_website={
            "url": "https://arcade.tw-smith.me",
            "desc": "arcade.tw-smith.me",
        },
        project_repo=[
            {
                "url": "https://github.com/tw-smith/arcade",
                "desc": "github.com/tw-smith/arcade",
            }
        ],
    )


@app.route("/projects/cyclingsouth.html", methods=["GET"])
def cyclingsouth():
    return render_template(
        "cyclingsouth_template.html",
        project_title="Cycling South Blog",
        project_image_url="../static/cyclingsouth_home_screely.png",
        project_website={
            "url": "https://cycling-south.com",
            "desc": "cycling-south.com",
        },
        project_repo=[
            {
                "url": "https://github.com/tw-smith/tourblog-strapi",
                "desc": "github.com/tw-smith/tourblog-strapi",
            },
            {
                "url": "https://github.com/tw-smith/tourblog-angular",
                "desc": "github.com/tw-smith/tourblog-angular",
            },
        ],
    )


@app.route("/projects/authserver.html", methods=["GET"])
def authserver():
    return render_template(
        "authserver_template.html",
        project_title="Authentication Server",
        project_image_url="../static/authserver_home_screely.png",
        project_website={
            "url": "https://github.com/tw-smith/auth-server",
            "desc": "github.com/tw-smith/auth-server",
        },
        project_repo=[
            {
                "url": "https://github.com/tw-smith/auth-server",
                "desc": "github.com/tw-smith/auth-server",
            }
        ],
    )
