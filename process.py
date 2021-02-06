from os import sys
import __main__ as main
from api import post_declare_logs
from excuses import excuses


def print_propositions():
    for i, MOD in enumerate(main.modules_list):
        print("{} : {}".format(i + 1, MOD["name"]))
    try:
        MODULE = input("\nSelectionnez un module \n")
        while int(MODULE) > len(main.modules_list) or int(MODULE) <= 0:
            MODULE = input("\nSelectionnez un module \n")
        print('\x1bc')
        for i, DATE in enumerate(main.schedules_list):
            print("{} : {}".format(i + 1, DATE["name"]))
        DATE = input("\nSelectionnez un jour\n")
        while int(DATE) > len(main.schedules_list) or int(DATE) <= 0:
            DATE = input("\nSelectionnez un jour\n")
        print('\x1bc')
        for i, HOUR in enumerate(main.hours_list):
            print("{} : {}".format(i + 1, HOUR["name"]))
        HOURS = input("\nSelectionnez les horaires\n")
        while(int(HOURS) > len(main.hours_list) or int(HOURS) <= 0):
            HOURS = input("\nSelectionnez les horaires\n")
        print('\x1bc')
    except KeyboardInterrupt:
        sys.exit()
    
    print_excuses(MODULE, DATE, HOURS)


def print_excuses(MODULE, DATE, HOURS):
    print("0\t: 0%")
    for i in range(10):
        print("{}\t: {}%".format((i + 1), (i + 1) * 10))
    print("11\t: Personnaliser")
    index_excuse = input("\nVeuillez indiquer à combien de pourcentage vous estimez votre projet terminé.\n\n")
    if int(index_excuse) == 11:
        try:
            JUSTIFICATION = {
                "objectif": input("Objectif :\n"),
                "action": input("\n\nActions :\n"),
                "resultat": input("\n\nRésultats :\n")
            }
        except KeyboardInterrupt:
            sys.exit()
    else:
        JUSTIFICATION = excuses[int(index_excuse)]
        
    post_declare_logs(MODULE, DATE, HOURS, JUSTIFICATION)