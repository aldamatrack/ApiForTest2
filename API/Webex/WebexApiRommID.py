import requests
import json
def getID():
    url = "https://webexapis.com/v1/rooms"

    payload={}
    headers = {
        'Authorization': 'Bearer OWRhODMzNjgtNWRhNy00YmIyLWI2ZWEtYjQzOGJkNTJhMWUzZmIwNDIxZDItYTFl_PF84_d3558e03-2933-4d83-8021-b115db9045d4'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    a = response.json()["items"]
    b = {}


    for i in a:
        b[i["title"]] = i["id"]
    return b


def postMessagesALL(dic):
    url = "https://webexapis.com/v1/messages"
    for i , x in dic.items():
        #print(x)
        payload = json.dumps({
        "roomId": x,
        "text": "hi from Python"
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer OWRhODMzNjgtNWRhNy00YmIyLWI2ZWEtYjQzOGJkNTJhMWUzZmIwNDIxZDItYTFl_PF84_d3558e03-2933-4d83-8021-b115db9045d4'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
a = getID()
print (a)
