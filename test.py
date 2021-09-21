
import requests
from requests.auth import HTTPDigestAuth
import json

# Replace with the correct URL
url = "http://127.0.0.1/start"

def go(id,link):
# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
    myResponse =requests.post(url, json={"id": str(id),"url":str(link)})
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
    if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content)
        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        for key in jData:
            print (key + " : " + str(jData[key]))
    else:
  # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
        
id=0
with open("test.txt","r") as f:
    for line in f:        
       go(str(id),line.strip())
       id=id+1