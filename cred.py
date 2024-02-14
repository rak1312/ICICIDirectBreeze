

import json
# load credentials from JSON file
f = open ('./cred.json', "r")
data = f.read()
json_data = json.loads(data)
f.close()


session_token = json_data['session_token']
app_key = json_data['app_key']
secret_key = json_data['secret_key']



#establish breeze connection
from breeze_connect import BreezeConnect
breeze = BreezeConnect(api_key=app_key)
breeze.generate_session(api_secret=secret_key, session_token=session_token)

print ("====Breeze session Connected=======")
import urllib
print("https://api.icicidirect.com/apiuser/login?api_key=" + urllib.parse.quote_plus(app_key))
