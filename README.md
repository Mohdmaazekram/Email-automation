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

* Error Handling: Includes error handling for both the main process and the email sending step, printing error messages if something goes wrong.
