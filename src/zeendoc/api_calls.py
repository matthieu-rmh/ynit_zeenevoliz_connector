import os
import json
from zeep import Client

def login(wsdl_client, login_credentials):

    # login **kwargs
    login_kwargs = {
            "Login": login_credentials["login"],
            "CPassword": login_credentials["cpassword"],
            "Password": login_credentials["password"],
            "Access_token": login_credentials["access_token"]
            }

    response = make_zeendoc_soap_request(wsdl_client.service.login, **login_kwargs)
    return json.loads(response)['Cookie']



def make_zeendoc_soap_request(method, **body_request):
    return method(**body_request)

def get_evoliz_data():
    print("evoliz data")

def test():
    # Get the directory of the current Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to config.json in the parent directory
    config_path = os.path.join(script_dir, "config.json")

# Load the JSON file
    with open(config_path, "r") as file:
        config = json.load(file)

    wsdl = config["wsdl"]
    print(wsdl)
    client = Client(wsdl=wsdl)

    cookie = login(client, config)
    print(f"cookie= {cookie}")

    print("inside zeendoc api calls")

