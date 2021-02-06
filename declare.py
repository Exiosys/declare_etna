#!/usr/bin/env python
# coding: utf-8
from datetime import date, timedelta
import requests
from authentification import authentification

SESSION = requests.Session()

TODAY = date.today()
YESTERDAY = TODAY - timedelta(days=1)
modules_list = []
schedules_list = [
    {"name": "Aujourd'hui", "date": TODAY.strftime("%Y-%m-%d")},
    {"name": "Hier", "date": YESTERDAY.strftime("%d/%m/%Y")}
]
hours_list = [
    {"name": "Journée (9h - 17h)", "time": ["09:00", "17:00"]},
    {"name": "Matin (9h - 12h)", "time": ["09:00", "12:00"]},
    {"name": "Midi (13h - 17h)", "time": ["13:00", "17:00"]},
    {"name": "Custom", "time": "0"},
]


def main():
    return authentification()


if __name__ == "__main__":
    main()
