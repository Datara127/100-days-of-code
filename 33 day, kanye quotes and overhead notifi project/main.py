import time
import requests
from datetime import datetime
import smtplib

my_email = "alexeylos2002@mail.ru"
password = "NU1BRx99KGPrvGVwgHGc"

MY_LAT = 56.010441  # Your latitude
MY_LONG = 37.846859  # Your longitude

M_LAT = 55.755825  # Your latitude
M_LONG = 37.617298  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="alexeylos02@gmail.com",
                msg=f"Subject: Look up\n\nThe ISS is above in the sky"
            )
    time.sleep(60000)
