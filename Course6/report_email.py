#!/usr/bin/env python3
import datetime
import os
import requests
import emails
from datetime import datetime
import run


if __name__ == "__main__":
     title="Processed Update on " + datetime.datetime.today().strftime('%B %d %Y')
     with open("reports.txt", "r") as file:
          paragraph=file.read()
     reports.generate_report("/tmp/processed.pdf", title, paragraph)
     sender = "automation@example.com"
     receiver = "{}@example.com".format(os.environ.get('USER'))
     subject = "Upload Completed - Online Fruit Store"
     body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"

     message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
     emails.send_email(message)
