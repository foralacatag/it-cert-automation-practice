#!/usr/bin/env python3
from datetime import datetime
import os
import requests
import emails
from datetime import datetime
import run
import reports

if __name__ == "__main__":
     title="Processed Update on " + datetime.today().strftime('%B %d, %Y')
     paragraph="/home/{}/report.txt".format(os.environ.get('USER'))
     reports.generate_reports("/tmp/processed.pdf", title, paragraph)
     sender = "automation@example.com"
     receiver = "{}@example.com".format(os.environ.get('USER'))
     subject = "Upload Completed - Online Fruit Store"
     body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"

     message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
     emails.send_email(message)
