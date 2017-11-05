#api demo

from urllib.request import urlopen
import json
import geocoder

"""
&location=42.3912%2C-72.5267%2C100&user_location=42.3912%2C-72.5267&skip=0&limit=10&user_key=349beaed7c0fbb0a3384f8e45209205a
"""
def betterdoctor_search(latlng, apiKey):
    url = "https://api.betterdoctor.com/2016-03-01/doctors?specialty_uid=psychologist&user_key=" + apiKey
    latlngUrl = str(latlng[0]) + "%2C" + str(latlng[1])
    locationUrl = "&location=" + latlngUrl + "%2C100&user_location=" + latlngUrl
    finalUrl = url + locationUrl + "&skip=0&limit=10"
    print(finalUrl)
    json_obj = urlopen(finalUrl)
    data = json.load(json_obj)
    dataJSON = data["data"]
    storage = []
    for docInfo in dataJSON:
        profile = docInfo["profile"]
        fname = profile["first_name"]
        lname = profile["last_name"]
        bio = profile["bio"]
        storage.append({
            "fname": fname,
            "lname": lname,
            "bio": bio
        })
        # print(fname + " " + lname + "\n" + bio + "\n\n\n")
    return storage

def betterdoctor_searchDriver():
    betterdoctor_api = "349beaed7c0fbb0a3384f8e45209205a"
    g = geocoder.ip("me")
    return betterdoctor_search(g.latlng, betterdoctor_api)
