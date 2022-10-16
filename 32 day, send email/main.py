from random import choice
import smtplib
import datetime as dt

now_date = dt.datetime.now()
day_of_week = now_date.weekday()

my_email = "alexeylos2002@mail.ru"
password = "NU1BRx99KGPrvGVwgHGc"

if day_of_week == 6:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
        random_quote = choice(quotes)

    with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="alexeylos02@gmail.com",
            msg=f"Subject:Random quote\n\n{random_quote}"
        )
