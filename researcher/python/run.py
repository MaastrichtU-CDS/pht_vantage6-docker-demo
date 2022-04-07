from vantage6.client import Client
from pathlib import Path
import time
import json

print("Attempt login to Vantage6 API")
client = Client("http://localhost", 5000, "/api")
client.authenticate("node1-user", "node1-password")
client.setup_encryption(None)

input_ = {
    "master": "true",
    "method":"master", 
    "args": [],
    "kwargs": {"column_name": "age"}
}

# Retrieve organization IDs to use
collaboration_list = client.collaboration.list()
collaboration_index = 0
organization_ids_ = [ ]
for organization in collaboration_list[collaboration_index]['organizations']:
    organization_ids_.append(organization['id'])

print("Requesting to execute summary algorithm")
task = client.post_task(
    name="RetrieveVariables",
    image="jaspersnel/v6-average-py",
    collaboration_id=collaboration_list[collaboration_index]['id'],
    input_= input_,
    organization_ids=[organization_ids_[0]]
)

print("Wait and fetch results")
res = client.result.get(id_=task.get("results")[0]['id'])
attempts=1
while((res["finished_at"] == None) and attempts < 10):
    print("waiting...")
    time.sleep(5)
    res = client.result.get(id_=task.get("results")[0]['id'])
    attempts += 1
print(res['result'])