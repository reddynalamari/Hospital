import smtplib
import ssl
from email.message import EmailMessage
import random

def mail_sender(name,id,email_receiver,bill,operation,problem,date):
    # Define email sender and receiver
    email_sender = 'your mail id'
    email_password = 'password'
    subject = 'SRAV Hospital'
    if operation == 'new':
        body = f"""
        Hello {name} you have successfully admitted in 
        SRAV hospital on {date}
        with id as {id} 
        and your current bill is {bill} 
        for {problem} 
        
        
        For any queries contact:-98657512**
        """
    elif operation == "edit":
        body = f"""
        Hello {name} your details are successfully changed in SRAV hospital
        Your id is {id} and your current bill is {bill}
        
        
        For any queries contact:-98657512**
        """
    else:
        body = f"""
                Hello {name} your details are successfully removed in SRAV hospital
                Your id is {id} and your current bill is {bill}


                For any queries contact:-98657512**
                """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
def otp_sender(email_receiver):
    otp = random.randrange(100000, 999999)
    email_sender = 'sravproject@gmail.com'
    email_password = 'vvkdnhgnahjhsbwn'
    subject = 'SRAV Hospital'
    body = f"""
            Your one time password for SRAV staff is {otp}


            For any queries contact:-98657512**
            """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return otp
