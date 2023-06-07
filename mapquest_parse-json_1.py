import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Santiago"
dest = "Ovalle"
key = "AwSjpGsi17MShL6uzEEwD9q4jHD0R9CB"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print("=============================================")
print("Direccion de origen " + (orig) + " direccion  de destino " + (dest))
print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
print("=============================================\n")
while True:
    q = input("Presione q o quit para salir:")
    if q == "quit" or q == "q":
        break
