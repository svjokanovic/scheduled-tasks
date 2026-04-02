import smtplib
import datetime as dt
import pandas as pd
import random

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day_now = now.day
month_now = now.month

birthdays = pd.read_csv("birthdays.csv")
birthdays_dict=birthdays.to_dict("records")
for birthday in birthdays_dict:
    if birthday["month"] == month_now:
        if birthday["day"] == day_now:
            num = random.randint(1,3)
            with open(f"./letter_templates/letter_{num}.txt", "r") as let:
                letter = let.read()
                new_letter = letter.replace("[NAME]", birthday["name"])

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday["email"],
                    msg=f"Subject:Happy birthday\n\n{new_letter}"
                )
