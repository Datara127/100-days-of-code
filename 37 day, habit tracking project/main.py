import requests
import datetime

USER = "datara"
TOKEN = "eyJhbGciOiJIUzI1"
GRAPHNAME = "graph1"

pixela_url = "https://pixe.la/v1/users"
pixela_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_url}/{USER}/graphs"
graph_config = {
    "id": GRAPHNAME,
    "name": "Cycloid Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.datetime.now()
today = today.strftime("%Y%m%d")
print(today)

add_graph_endpoint = f"{graph_endpoint}/{GRAPHNAME}"
add_graph_config = {
    "date": today,
    "quantity": "20.4",
}

put_graph_endpoint = f"{add_graph_endpoint}/{today}"
put_graph_config = {
    "quantity": "25"
}

response = requests.delete(url=put_graph_endpoint, json=put_graph_config, headers=headers)
print(response.text)
