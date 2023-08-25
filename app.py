from flask import Flask, render_template, redirect, request, url_for
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage



app = Flask(__name__)
app.static_folder = 'static'
app.static_url_path = '/static'
app = Flask(__name__, static_url_path='/static', static_folder='static')



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/sendemial", methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        email = "techlife5220@gmail.com"
        password = "98824@5220"

    # email account server
    server = smtplib.SMTP('smtp.gmail', 587)
    server.ehlo()
    server.starttls()
    server.login("techlife5220@gmail.com", "98824@5220")

    # sender and receiver's email address
    msg = EmailMessage()
    msg.set_content("First Name : "+str(name) +"\nEmail: "+str(email)+"\Subject: "+str(subject)+"\nMesssage: "+str(message))

    msg['To'] = email
    msg['From'] = "techlife5220@gmail.com"
    msg['Subject'] = subject

     # Send the message via our own SMTP server.
    try:
         # sending an email
        server.send_message(msg)
        print("Send")
    except:
            print("Fail to Send")
            pass

if __name__ == "__main__":
    app.run(debug=True)