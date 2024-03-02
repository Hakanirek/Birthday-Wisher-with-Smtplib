import pandas as pd
import smtplib
import datetime as dt
import random

PLACE_HOLDERS = "[NAME]"

MY_EMAIL = "Your Mail Address"
MY_PASSWORD = "Your Password"


today_date = dt.datetime.now()
today_tuple = (today_date.month, today_date.day)

birthdays = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person= birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACE_HOLDERS, birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")
