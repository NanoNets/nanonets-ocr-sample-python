import requests, os, json
  
url = "https://app.nanonets.com/api/v2/ObjectDetection/Model/"
api_key = os.environ.get('NANONETS_API_KEY')

##
payload = "{\"categories\" : [\"number_plate\"], \"model_type\": \"ocr\"}"
headers = {'Content-Type': "application/json",}

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(api_key, ''), data=payload)
model_id = json.loads(response.text)["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")