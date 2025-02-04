from oauth2client.service_account import ServiceAccountCredentials
from glob import glob
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
from email.header import decode_header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import concurrent.futures
from io import StringIO
import pandas_gbq as pg
import smtplib
import pandas as pd
import numpy as np
import db_dtypes
import requests
import random
import socket
import json
import time
import re
import os
import io


import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Function to generate initials from customer name
def get_initials(name):
    initials = ''.join([part[0].upper() for part in name.split() if part])
    return initials

# Define the column names
columns = [
    'Customer_Name', 'contactNumber', 'gender', 'ageGroup', 'lookingFor',
    'budget', 'occasion', 'occasionOther', 'knowAbout', 'knowAboutOther',
    'timeSpent', 'reason', 'agentCode', 'Date', 'invoiceNumber', 'code',
    'inventory_loction', 'initial', 'store_type', 'id', 'status', 'name',
    'email', 'phone', 'photo', 'address', 'agent_code', 'agent_commission',
    'created', 'store_id', 'store_code', 'agent_password',
    'datastream_metadata', 'start_date', 'Store', 'synergics_invoice_id',
    'revenue', 'Total_No_of_Days', 'WeekDay', 'WeekEnd'
]

# Function to generate dummy data
def generate_dummy_data(num_rows):
    data = {
        'Customer_Name': [fake.name() for _ in range(num_rows)],
        'contactNumber': [fake.phone_number() for _ in range(num_rows)],
        'gender': [random.choice(['Male', 'Female', 'Other']) for _ in range(num_rows)],
        'ageGroup': [random.choice(['18-25', '26-35', '36-45', '46-60', '60+']) for _ in range(num_rows)],
        'lookingFor': [random.choice(['Product', 'Service', 'Information']) for _ in range(num_rows)],
        'budget': [random.randint(50, 5000) for _ in range(num_rows)],
        'occasion': [random.choice(['Birthday', 'Wedding', 'Anniversary', 'Corporate', 'Other']) for _ in range(num_rows)],
        'occasionOther': [random.choice([None, 'Custom Event']) for _ in range(num_rows)],
        'knowAbout': [random.choice(['Social Media', 'Friends', 'Advertisement', 'Website', 'Other']) for _ in range(num_rows)],
        'knowAboutOther': [random.choice([None, 'Search Engine', 'Magazine']) for _ in range(num_rows)],
        'timeSpent': [random.randint(5, 120) for _ in range(num_rows)],  # in minutes
        'reason': [random.choice(['Interested', 'Gift', 'Promotions', 'Other']) for _ in range(num_rows)],
        'agentCode': [fake.uuid4() for _ in range(num_rows)],
        'Date': [fake.date_this_decade() for _ in range(num_rows)],
        'invoiceNumber': [fake.uuid4() for _ in range(num_rows)],
        'code': [random.choice(['A1', 'B2', 'C3', 'D4', 'E5']) for _ in range(num_rows)],
        'inventory_loction': [random.choice(['Warehouse 1', 'Warehouse 2', 'Store 1', 'Store 2']) for _ in range(num_rows)],
        'initial': [get_initials(fake.name()) for _ in range(num_rows)],  # Using custom function to generate initials
        'store_type': [random.choice(['Retail', 'Online', 'Both']) for _ in range(num_rows)],
        'id': [random.randint(1000, 9999) for _ in range(num_rows)],
        'status': [random.choice(['Active', 'Inactive', 'Pending']) for _ in range(num_rows)],
        'name': [fake.name() for _ in range(num_rows)],
        'email': [fake.email() for _ in range(num_rows)],
        'phone': [fake.phone_number() for _ in range(num_rows)],
        'photo': [fake.image_url() for _ in range(num_rows)],
        'address': [fake.address() for _ in range(num_rows)],
        'agent_code': [fake.uuid4() for _ in range(num_rows)],
        'agent_commission': [random.uniform(0, 20) for _ in range(num_rows)],
        'created': [fake.date_this_year() for _ in range(num_rows)],
        'store_id': [random.randint(1, 50) for _ in range(num_rows)],
        'store_code': [random.choice(['S001', 'S002', 'S003', 'S004']) for _ in range(num_rows)],
        'agent_password': [fake.password() for _ in range(num_rows)],
        'datastream_metadata': [fake.text(max_nb_chars=50) for _ in range(num_rows)],
        'start_date': [fake.date_this_decade() for _ in range(num_rows)],
        'Store': [random.choice(['Store A', 'Store B', 'Store C']) for _ in range(num_rows)],
        'synergics_invoice_id': [fake.uuid4() for _ in range(num_rows)],
        'revenue': [random.uniform(100.0, 10000.0) for _ in range(num_rows)],
        'Total_No_of_Days': [random.randint(1, 30) for _ in range(num_rows)],
        'WeekDay': [random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']) for _ in range(num_rows)],
        'WeekEnd': [random.choice(['Saturday', 'Sunday']) for _ in range(num_rows)],
    }

    return pd.DataFrame(data)

# Generate dummy data for 100 rows
df = generate_dummy_data(100)


# Create a mapping for the email addresses based on the 'inventory_loction' values
location_email_map = {
    'Warehouse 1': 'maaz.ekram@xyz.com',
    'Warehouse 2': 'yash.dholam@xyz.com',
    'Store 2': 'mahanand.yadav@xyz.com',
    'Store 1': 'sabir.chougle@xyz.com'
}

# Create the new 'email' column based on the 'inventory_loction' value
df['email'] = df['inventory_loction'].map(location_email_map)


inventory_loction_lst = set(df['inventory_loction'])
inventory_loction_lstt = list(inventory_loction_lst)

for inventory_loction_lst in inventory_loction_lstt:
    filtered_data = df[df['inventory_loction'] == inventory_loction_lstt]

    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from datetime import date

    today = date.today()

    sub = 'Store Walkin Report Date :' + str(today)

    username = 'maaz.ekram@xyz.com'
    password = 'rivi dvht delj hgdn'

    # recipients
    recipients = filtered_data['email'].tolist()

    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = 'maaz.ekram@xyz.com'

    html = """
    <html>
    <h4>Hello Teams,</h4>
    <h4>Please find below Today’s Store Walkin Data Summary.</h4>
    </html>
    """
    part1 = MIMEText(html, 'html')
    msg.attach(part1)


    html = """
    <html>
    <h4>Todays Walkins Data</h4>
    <body> {0} </body>
    <br></br>
    </html>
    """.format(filtered_data.to_html(index=False))

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('maaz.ekram@xyz.com', 'rivi dvht delj hgdn')
        server.sendmail(msg['From'], emaillist, msg.as_string())
        server.close()
    except Exception as e:
        e