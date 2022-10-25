import requests
import smtplib

my_email = "alexeylos2002@mail.ru"
password = "NU1BRx99KGPrvGVwgHGc"
api_key = "69f04e4613056b159c2761a9d9e664d2"
lat = 56.010441
lon = 37.846859

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][7:19]
will_rain = False

for hour_data in weather_slice:
    conditional_data = hour_data["weather"][0]["id"]
    if conditional_data < 700:
        will_rain = True

with smtplib.SMTP("smtp.mail.ru", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        if will_rain:
            connection.sendmail(
                from_addr=my_email,
                to_addrs="alexeylos02@gmail.com",
                msg=f"Subject:Weather alert\n\nPick the umbrella."
            )
        else:
            connection.sendmail(
                from_addr=my_email,
                to_addrs="alexeylos02@gmail.com",
                msg=f"Subject:Weather alert\n\nDont pick the umbrella."
            )


