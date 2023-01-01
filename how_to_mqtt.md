# envoi mqtt

Envoyer vers AWS IOT core 

-> topic à utiliser  "bike-tracking/+/data" 
on change le + avec le nom du device 
par ex: "bike-tracking/tracker/data"


# format des données 

````json
{
    "msg_type": "alert",
    "position": {
        "latitude": 12,
        "longitude": 12,
        "altitude": 12
    }

}
````