from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from pretty_html_table import build_table
import pandas as pd
from smtplib import SMTP
import logging
import os

SuccessCount = 0
FailureCount = 0
SkippedCount = 0
Success_List = []
Failure_Cause = []
Execution_time = []

SENDER_MAIL = 'TestMailPrimeQA@gmail.com'
SENDER_PWD = '*******'
Tester = 'sachin@primeqasolutions.com'
cc = 'sachin@primeqasolutions.com,devanshi@primeqasolutions.com'
Recipents = cc.split(",") + [Tester]


def Success_List_Append(testID, Time_taken, Status_Code):
    global SuccessCount, FailureCount
    Success_List.append([testID, Time_taken, Status_Code])
    SuccessCount += 1
    logging.info(f"Time taken for {testID} is {Time_taken} with status code {Status_Code}")

def TestReport_Generation():
    global Test_Report_Table
    print("Entered into TestReport_Generation()")
    Test_Report = [["Project Name", "DEMO"], ["Test Type", "Automation"],
                    ["Total Test Cases", int(SuccessCount + FailureCount)]]
    Test_Report_DF = pd.DataFrame(Test_Report, columns=("Summary", "Details"))
    Test_Report_Table = build_table(Test_Report_DF, "blue_dark", text_align='justify')
    print("Exiting from TestReport_Generation()")


def Summary_Table_Formation():
    global Summary_Table
    global Failure_Cause_Table
    Summary_table_DF = pd.DataFrame(Success_List, columns=["TestCase", "Time Taken", "Status Code"])
    Summary_Table = build_table(Summary_table_DF, "green_dark", text_align='justify')
    if FailureCount != 0:
        Failure_Cause_Table_DF = pd.DataFrame(Failure_Cause,
                                              columns=["TestCase No.", "TestCases Summary", "Failure Cause"])
        Failure_Cause_Table = build_table(Failure_Cause_Table_DF, "red_dark", text_align='justify')


def Send_Mail():
    print("Sending Mail...........")
    message = MIMEMultipart()
    message['Subject'] = 'Demo Results'
    message['From'] = SENDER_MAIL
    message['To'] = Tester
    message['Cc'] = cc
    # style='height: 500px; overflow: auto; width: fit-content'
    if FailureCount != 0:
        empanelled = "<p>Failure Cause Table</p><div>" + Failure_Cause_Table + "</div>"
    else:
        empanelled = "<p>No Failure Observed.</p>"
    html = """\
    	<html>
    	  <head></head>
    	  <body>
    	    <p>Hi,<br>
    	        Please find below Test Report for Automation Testing
    	    </p>
    	    <p>Test Report/Details
    	    </p>
    	    <div>""" + Test_Report_Table + """
    	    </div>
    	    <p>Summary Table
    	    </p>
    	    <div >""" + Summary_Table + """
    	    </div>
    	    <p>""" + empanelled + """</p>
    	    <p>THIS IS SYSTEM GENERATED MAIL.</p>
    	    <p></p>
    	  </body>
    	</html>
    	"""

    part2 = MIMEText(html, 'html')
    message.attach(part2)
    filename = os.path.join(os.getcwd(), "pytest.log")
    attachment = open(filename, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= Logs")
    message.attach(part)
    msg_body = message.as_string()
    try:
        server = SMTP('smtp.gmail.com', 587)
        # outlook = client.Dispatch("Outlook.Application")
        server.starttls()
        server.login(message['From'], SENDER_PWD)
        server.sendmail(message['From'], Recipents, msg_body)
        server.quit()
        print("Mail Sent successfully")
    except Exception as e_mail:
        print("Mail sending Failed")
        print(e_mail)
