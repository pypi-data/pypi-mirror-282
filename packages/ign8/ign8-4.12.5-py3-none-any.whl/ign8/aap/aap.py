import requests
import os
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def default_secrets():
    return {
        "client_id": os.getenv("AAP_CLIENT_ID"),
        "client_secret": os.getenv("AAP_CLIENT_SECRET"),
        "username": os.getenv("AAP_USERNAME"),
        "password": os.getenv("AAP_PASSWORD"),
    }



def status():
    #We need to create an ascii menu that shows the status of the AAP
    #We need to show the status of the AAP

    print("AAP Status")
    print("==========")
    print("Checking AAP Status")
    print("Please wait...")
    print(default_secrets())
    print("....")


    