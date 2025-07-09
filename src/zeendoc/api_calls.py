import os
import json
from zeep import Client

def login():

# Get the directory of the current Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json in the parent directory
    config_path = os.path.join(script_dir, "config.json")

# Load the JSON file
    with open(config_path, "r") as file:
        config = json.load(file)

    # print(config)

    # wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
    wsdl = "https://armoires.zeendoc.com/lrc/ws/3_1/wsdl.php?WSDL"
    print(wsdl)
    client = Client(wsdl=wsdl)
    response = client.service.login(
            Login=config["login"],
            CPassword=config["cpassword"],
            Password=config["password"],
            Access_token=config["access_token"]
        )

    print(response)

def test():
    print("inside zeendoc api calls")

