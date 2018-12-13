from flask_mail import Message
from application import mail


def send(sender_email, sender_subject, message):
        # recipients=["2018singcolor@gmail.com"]
        msg = Message(f'From {sender_email}, My Blog',
                sender='noreply@demo.com',
                recipients=["s777610@gmail.com"])  
        msg.body = f"""
        From: {sender_email}
        Subject: {sender_subject}
        Message: {message}
        """
        mail.send(msg)