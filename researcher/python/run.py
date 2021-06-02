from vantage6.client import Client
from pathlib import Path
import time

print("Attempt login to Vantage6 API")
client = Client("http://localhost", 5000, "/api")
client.authenticate("node1-user", "node1-password")
client.setup_encryption(None)

input_ = {
    "master": "true",
    "method":"master", 
    "args": [
        {
            "PatientID":"category",
            "age":"float64", 
            "Clinical.T.Stage":"category", 
            "Clinical.N.Stage":"category",
            "Clinical.M.Stage": "category",
            "Overall.Stage": "category",
            "Histology": "category",
            "gender": "category",
            "Survival.time": "Int64",
            "deadstatus.event": "Int64"}, 
        ".",#decimal indicator
        ","],#CSV delimiter
    "kwargs": {}
}

print("Requesting to execute summary algorithm")
task = client.post_task(
    name="testing",
    image="harbor.vantage6.ai/algorithms/summary",
    collaboration_id=client.collaboration.list()[0]['id'],#Get the first collaboration associated with user
    input_= input_,
    organization_ids=client.collaboration.list()[0]['organizations'][0]['id']#Get first org in the collaboration to run the algorithm on
)

print("Wait and fetch results")
res = client.result.get(id_=task.get("results")[0]['id'])
attempts=1
while((res["finished_at"] == None) and attempts < 30):
    print("waiting...")
    time.sleep(5)
    res = client.result.get(id_=task.get("results")[0]['id'])
    attempts += 1

print(res['result'])