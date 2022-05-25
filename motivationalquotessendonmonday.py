import datetime as dt
import smtplib
import random

my_email = "mrwickjonathan62@gmail.com"
my_password = "abc123()"

now = dt.datetime.now()
week_of_the_day = now.weekday()
print(week_of_the_day)
week_day = 7


with open("quotes.txt") as file:
    quotes = file.readlines()
# print(len(quotes))


random_quotes = random.randint(0, 27 - 1)
day_random_quotes = quotes[random_quotes - 1]
# print(day_random_quotes)

if week_day == 7:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="mrwickjonathan62@yahoo.com", msg=day_random_quotes)
    connection.close()