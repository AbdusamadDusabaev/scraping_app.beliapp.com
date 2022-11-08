import json
import requests
import csv


file_name = "restaurants.csv"
with open(file_name, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Categories", "Neighborhood", "City", "Rating"])

response = requests.get(url="https://beli.cleverapps.io/api/rank-list/7b002fa2-74dd-4478-a923-366223e67486/")
json_objects = response.json()
for json_object in json_objects:
    name = json_object["business__name"]
    if not json_object["business__price"] is None:
        dollars = "$" * json_object["business__price"]
    else:
        dollars = "None"
    categories = ", ".join(json_object['business__cuisines'])
    neighborhood = json_object["business__neighborhood"]
    city = json_object["business__city"]
    rating = json_object["score"]
    result = [name, dollars, categories, neighborhood, city, rating]
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(result)
