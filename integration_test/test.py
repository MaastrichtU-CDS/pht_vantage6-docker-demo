import unittest
#from vantage6.client import Client
import vantage6.client as v6

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.__apiUrl = "http://localhost"
        self.__port = 5000
        self.__apiPath = "/api"
        self.__username = "johan"
        self.__password = "1234"
    
    # @classmethod
    # def tearDownClass(cls):
    #     cls._connection.destroy()

    def test_login(self):
        client = v6.Client(self.__apiUrl, self.__port, self.__apiPath)
        client.authenticate(self.__username, self.__password)

        client.setup_encryption(None)
        self.assertEqual(client.name, "Johan")

    # def test_summary(self):
    #     print("Attempt login to Vantage6 API")
    #     client = Client(self.__apiUrl, self.__port, self.__apiPath)
    #     client.authenticate(self.__username, self.__password)

    #     client.setup_encryption(None)

    #     input_ = {
    #         "master": "true",
    #         "method":"master", 
    #         "args": [
    #             {
    #                 "ID":"Int64",
    #                 "Age":"Int64", 
    #                 "Clinical.T.Stage":"category", 
    #                 "Clinical.N.Stage":"category",
    #                 "Clinical.M.Stage": "category",
    #                 "Overall.Ajcc.Stage": "category",
    #                 "Histology": "category",
    #                 "Sex": "category",
    #                 "Survival.Time.Days": "Int64",
    #                 "deadstatus.event": "Int64"}, 
    #             ".",
    #             ";"], 
    #         "kwargs": {}
    #     }

    #     print("Requesting to execute summary algorithm")
    #     task = client.post_task(
    #         name="testing",
    #         image="harbor.vantage6.ai/algorithms/summary",
    #         collaboration_id=1,
    #         input_= input_,
    #         organization_ids=[1, 2]
    #     )

    #     print("Wait and fetch results")
    #     res = client.get_results(task_id=task.get("id"))
    #     attempts=1
    #     while((res[0]["result"] == None) and attempts < 7):
    #         print("waiting...")
    #         time.sleep(5)
    #         res = client.get_results(task_id=task.get("id"))
    #         attempts += 1
    #     print(res[0]["result"])


if __name__ == '__main__':
    unittest.main()