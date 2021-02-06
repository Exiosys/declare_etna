import os
from getpass import getpass
from os import path, sys
from dotenv import load_dotenv


def get_env(var):
    load_dotenv()
    return os.getenv(var)
    
    
def check_env():
    if not path.exists(".env"):
        file = open(".env", "w") 
        try:
            file.write("LOGIN={}\n".format(input("Entrez votre login\n"))) 
            file.write("PASSWORD={}\n".format(getpass("Entrez votre mot de passe\n"))) 
        except KeyboardInterrupt:
            sys.exit()
        file.close() 
        
        
def remove_env():
    os.remove(".env")
