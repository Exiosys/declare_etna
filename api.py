import requests
import __main__ as main
from helper import get_env
import moment


def get_modules():
    REQUEST = main.SESSION.get("https://modules-api.etna-alternance.net/students/{}/search".format(get_env("LOGIN")))
    RESPONSE = REQUEST.json()

    for UV in RESPONSE:
        if "ETN" not in UV["uv_name"]:
            main.modules_list.append({
                'id':UV["id"], 
                'uv_id': UV["uv_id"], 
                'name': "{} - {}".format(UV["uv_name"], UV["long_name"])
            })
   
   
def get_schedules():
    URL = "https://gsa-api.etna-alternance.net/students/{}/schedules_current_run".format(get_env("LOGIN"))
    REQUEST = main.SESSION.get(URL)
    RESPONSE = REQUEST.json()["contracts"][0]["schedules"]
    
    for DATE in RESPONSE:
        DATE = moment.date(DATE["start"])
        DATA = {
            "name": "Le {}".format(DATE.format("D/M/YYYY")),
            "date": DATE.format("YYYY-M-D")
        }
        main.schedules_list.append(DATA)
         
         
def post_declare_logs(index_module , index_day, index_hours, excuse):
    MODULE = main.modules_list[int(index_module) - 1]["id"]
    DATE = main.schedules_list[int(index_day) - 1]["date"]
    HOURS = main.hours_list[int(index_hours) - 1]["time"]
    OBJECTIFS = excuse["objectif"]
    ACTIONS = excuse["action"]
    RESULTAT = excuse["resultat"]
    
    # parameters = {"module":7556,"declaration":{"start":"2021-02-6 3:00","end":"2021-02-6 4:00","content":"Objectifs :\nTester mes déclarations\nActions :\n Je fais un déclaratif\nRésultats :\nJe sais pas encore \nDifficultés rencontrées :\n RAS"},"sosJawa": 0}
    parameters = {
        "module": MODULE,
        "declaration": {
            "start": "{} {}".format(DATE, HOURS[0]),
            "end": "{} {}".format(DATE, HOURS[1]),
            "content":
                 "Objectifs :\n{}\nActions :\n{}\nRésultats :\n{}\nDifficultés rencontrées :\n RAS".format(OBJECTIFS, ACTIONS, RESULTAT)
        },
        "sosJawa":  0
    }
    
    URL = "https://intra-api.etna-alternance.net/modules/{}/declareLogs".format(MODULE)
    REQUEST = main.SESSION.post(URL, json=parameters)
    
    if(REQUEST.status_code == 200):
        print("Déclaration envoyée !")
    else:
        print("Une erreur est survenue ..")
    
    