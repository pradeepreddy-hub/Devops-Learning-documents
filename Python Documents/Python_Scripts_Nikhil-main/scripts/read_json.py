import json
import sys
import requests
import tarfile

with open("/home/ubuntu/python/python/1.json", "r") as fh:
    json_data=json.load(fh)
    #print(json_data)
file_path="/home/ubuntu/behave.tar.gz"
for ele in json_data:
    #  for key, value in ele.items():
    source_url=ele["Source URL"]
    response = requests.get(source_url)
   # response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("Tar file downloaded successfully.")
    break
print("outside the for loop")


file = tarfile.open('/home/ubuntu/behave.tar.gz')
# extracting a specific file
file.extract('/home/ubuntu')
    #print(ele["Source URL"])
        #print(key)
        #print(value)
    #print("-----------------------------------------")


    #print(ele)
   # sys.exit()
