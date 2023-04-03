import smtplib
import random
import pandas
from datetime import datetime

##################### Hard Starting Project ######################

user_mail = "umuttbasarann@gmail.com"
user_password = "gqbuyufzdciayuic"
to_mail = "techwithzanzi@gmail.com"

today_date = datetime.now()
today = (today_date.month, today_date.day)

data = pandas.read_csv("birthdays.csv")

birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays:
    birthday_person = birthdays[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        updated_contents = contents.replace("[NAME]", birthday_person["name"])


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=user_mail, password=user_password)
    connection.sendmail(from_addr=user_password, to_addrs=to_mail, msg=f"Subject:Happy Birthday!\n\n"
                                                                       f"{updated_contents}")


