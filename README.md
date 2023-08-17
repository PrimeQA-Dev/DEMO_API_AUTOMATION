# Sample_API_AUTOMATION

This is a sample project outline for implementing API automation using Python with the Pytest framework. This is a great way to structure your automation efforts. 

Here's a breakdown of the steps you've outlined:

**1. Success and Failure Lists:**
You likely plan to maintain separate lists or data structures to keep track of successful and failed API calls. This will help you categorize and analyze the test results easily.

**2. Generate Own Report:**
You're planning to generate a custom test report. This could involve using the -HTML flag provided by Pytest to generate an HTML report detailing the test execution results.

**3. Trigger Mail Post Execution:**
After the test execution is complete, you plan to send an email containing the test report as the email body. This would involve integrating with an email library or service to send emails programmatically.

**4. Generate Log File and Attach to Email:**
You intend to create a log file to capture relevant information about the test execution. This log file will then be attached to the email along with the test report.





**How to Run:**
You've provided instructions on how to run the automation project:

Clone the project from its repository.

Navigate to the project's folder path using the terminal.

Run the command python -m pytest -html=report.html to execute the test cases and generate the HTML report.


**To Generate Report**

Provide mail ID details in the report_mail.py file to receive the mail post-execution.
   
