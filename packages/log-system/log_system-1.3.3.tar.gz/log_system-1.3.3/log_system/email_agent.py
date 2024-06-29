from multiprocessing import Process
import pandas as pd
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import atexit
import json
from os.path import join as pjoin
import sys

EMAIL_SYSTEM_VERSION="1.0.6"
NOTIFICATION_DIR=pjoin(os.path.dirname(os.path.abspath(__file__)), "notification")

class EmailNotificationSystem:
    def __init__(self, email_configs):
        self.email_credential = {"email_address":email_configs["email_sender"],
                                 "password":email_configs["email_password"],
                                 "server_address":email_configs.get("server_address", "smtp.office365.com"),
                                 "server_port":email_configs.get("server_port", 587),
                                 }


    def send_email(self, subject, body, to_email):
        EmailNotificationSystem.email_sender(subject, body, to_email, self.email_credential)

    @staticmethod
    def email_sender(subject, body, to_email, email_credential):
        assert to_email!=[], "No recipient provided"
        sender_email = email_credential["email_address"]
        sender_password = email_credential["password"]
        server_address=email_credential.get("server_address", "smtp.office365.com")
        server_port=email_credential.get("server_port", 587)

        # Create the MIMEText object and set up headers
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email if not isinstance(to_email, list) else ", ".join(to_email)
        msg["Subject"] = subject
        msg.attach(MIMEText(subject + "\n\n" +body, "plain"))

        try:
            with smtplib.SMTP(server_address, server_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, to_email, msg.as_string())
                print("Email sent successfully!")
        except Exception as e:
            print("Failed to send email: ", e)
    
    @staticmethod
    def collect_pending_email(folder_path=NOTIFICATION_DIR):
        for subfolder_name in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder_name)
            
            # Check if the item is a directory to ensure depth 1 subfolders are processed
            if os.path.isdir(subfolder_path):
                content = []  # Initialize the list to hold JSON content for this subfolder
                
                # Iterate through each file in the subfolder
                for filename in os.listdir(subfolder_path):
                    file_path = os.path.join(subfolder_path, filename)
                    
                    # Ensure the file is a JSON file before processing
                    if os.path.isfile(file_path) and filename.endswith('.json'):
                        with open(file_path, 'r') as json_file:
                            try:
                                data = json.load(json_file)
                            except json.JSONDecodeError:
                                continue  # Skip files that cannot be decoded as JSON
                            
                            # Add the filename to the data
                            data['file_path'] = file_path
                            data["severity_level"] = filename.split("_") 
                            content.append(data)
                if len(content)==0:
                    continue
                # Yield the nested dictionary for the current subfolder
                yield {"task_type": subfolder_name, "content": content}


    @staticmethod
    def routine_email_sender(contact_df, email_credential, folder_path=NOTIFICATION_DIR):
        email_tasks_iter=EmailNotificationSystem.collect_pending_email(folder_path=folder_path)
        for emails in email_tasks_iter:
            # print("\n","---"*10,"\n")
            task_recipients = contact_df[((contact_df["alert_task_type"]==emails["task_type"]) | (contact_df["alert_task_type"]=="ADMIN"))]
                                  
            for email in emails["content"]:
                recipients = task_recipients[contact_df["severity_level"].isin([email["severity_level"], "ALL"])]["contact_email"].to_list()
                if len(recipients)>0:
                    EmailNotificationSystem.email_sender(email["subject"], email["body"], recipients, email_credential)
                os.remove(email["file_path"])
    
    version_info = {
            "1.0.1": "Create file level notification system base on splited out part of log system",
            "1.0.2": "Add recipents non empty check. Filter out non-configured email alerts",
            "1.0.3": "Update class name. Add init function to avoid duplicated email credential",
            "1.0.4": "Add configurable server_address and server_port",
            "1.0.5": "Add alert_task_type 'ADMIN' and severity_level 'ALL'; Optimized logic for discarding email",
            "1.0.6": "Add subject info to email boday; Add and support new severity_level 'Alert'"
            }
    

if __name__ == "__main__":
    arg1 = sys.argv[1]
    input_dict = json.loads(str(arg1))

    contact_df=pd.read_csv(input_dict["contact_info"])
    email_credential=input_dict["email_credential"]

    EmailNotificationSystem.routine_email_sender(contact_df, email_credential)