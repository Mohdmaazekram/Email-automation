# Automated Weekly Email Report for Product Descriptions

To develop a Python script that automatically generates and sends a weekly email report to the relevant department, detailing the count of products with missing or null descriptions in the website. This automation aims to streamline communication and ensure timely updates, facilitating better data management and departmental coordination.

Here are the steps to perform this project:
* Imports Libraries: The function imports various Python libraries for handling data, emails, Google Cloud storage, and BigQuery.

* Setup: Defines paths, dates, and sets up the environment, including temporary file locations.

* Query BigQuery: Runs a SQL query on Google BigQuery to retrieve SKUs without descriptions from a specific dataset.

* Process Data: Converts the query result into an Excel file using Pandas and saves it to a temporary location.

* Upload to Cloud Storage: Uploads a daily-updated Excel file to Google Cloud Storage and sends an email with the updated file upon function trigger.
  
* Email Setup: Prepares an email with HTML content to inform recipients about SKUs with missing descriptions.

* Send Email: Sends the email to a list of recipients using Gmail’s SMTP server.

* Error Handling: Includes error handling for both the main process and the email sending step, printing error messages if something goes wrong.\n

---

**Steps to Send Automatic Emails Using Python**

**1. Enable IMAP Access in Gmail:**

  * **IMAP (Internet Message Access Protocol)** is a protocol that allows you to access and manage your emails on a remote mail server. It enables you to read and organize emails without downloading them to your device. By enabling IMAP, you allow Python scripts or other applications to send and receive emails from your Gmail account programmatically.

  * To enable IMAP:
    
    * Open your Gmail account.
    * Go to **Settings** (click on the gear icon in the top right corner).
    * Click on **See all settings.**
    * Navigate to the **Forwarding and POP/IMAP** tab.
    * Enable **IMAP Access** and click **Save Changes.**
    * If prompted, verify that it’s you and confirm the changes.
      
**2. Enable Two-Step Verification and Create an App Password:**

  * To securely access your Gmail account via a script, you need to enable **Two-Step Verification** and create an **App Password.** The App Password is a 16-character password that allows apps to connect to your account without using your main Gmail password.
  
  * To create an App Password:
    
    * Search for "App Passwords" in your Google account help section.
    * Click on **Sign in with App Passwords** under Gmail Help.
    * In the **Create & use App Passwords** section, follow the instructions to generate an App Password.
    * You’ll receive a password in the format: <strong>rivi dvht delj kgrp</strong> (this will be used in your script).

**3. Create Python Code to Send Automatic Emails:**

Below is a sample Python code to send automated emails:
Please Find Example code from the Above Email Code File.
    
**Explanation of the Code:**

  * **sender_email:** Your Gmail address (e.g., your-email@gmail.com).
  * **app_password:** The app password you generated earlier.
  * **recipients:** A list of email addresses where you want to send the email.
  * **msg:** A multipart message with subject, sender, and HTML content.
  * The script connects to Gmail's SMTP server, logs in with your credentials, and sends the email to the recipients.

**4. Understanding SMTP:**

  * **SMTP (Simple Mail Transfer Protocol)** is the protocol used to send emails from one server to another. It is essential for sending emails programmatically using Python or other applications. When you use the Python smtplib library, you are interacting with an SMTP server (like Gmail’s server) to send your email.
  
  * In the script, we connect to Gmail's SMTP server (smtp.gmail.com) on port 587, log in using the email and app password, and send the email.
