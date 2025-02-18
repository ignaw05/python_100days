import smtplib
import datetime as dt
import pandas


my_password = "zyuv bbxe dpyw vifd"



birthdays = pandas.read_csv("birthdays.csv")
dictionary = birthdays.to_dict(orient="records")
print(dictionary)
today = (dt.datetime.now().day,dt.datetime.now().month)

for person in dictionary:
    if person['month'] == today[1] and person['day']==today[0]:
        name = person['name']
        with open("letter.txt") as file:
            new_text = []
            text_file = file.readlines()
            for line in text_file:
                new_line = line.replace('[NAME]', name)
                new_text.append(new_line)


            my_email = "ignaciowuilloud@gmail.com"
            connection = smtplib.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="wuilloudi@gmail.com",
                msg=f"Subject:Happy Birthday!\n\n{"".join(new_text)}")
            connection.close()