import requests

MES_URL = "http://192.168.1.56:3003"

def get_test_stations():
    full_url = MES_URL + "/test-stations/"
    response = requests.get(
        full_url,
        params={
            "skip": 0,
            "limit": 100
        }
    )
    print(response.status_code)
    print(response.text)
    return response
    
def post_test_stations():
    full_url = MES_URL + "/test-stations/"
    response = requests.post(
        full_url,
        json={
            "Name": "TH_TEST002",
            "Description": "TH_TEST001"
        }
    )
    print(response.status_code)
    print(response.text) 
    return response
    
def get_tests(test_station_uuid :str):
    full_url = MES_URL + "/tests/"
    response = requests.get(
        full_url,
        params={
            "Skip": 0,
            "Limit": 100,
            "TestStationUUID" :test_station_uuid
        }
    )
    print(response.status_code)
    print(response.text)
    return response

def post_tests(test_station_uuid:str, name:str, description:str):
    full_url = MES_URL + "/tests/"
    response = requests.post(
        full_url,
        json={
            "Name": name,
            "Description": description,
            "TestStationUUID": test_station_uuid,
            "Metadata": {
                    "key": "value",
                },
        }
    )
    print(response.status_code)
    print(response.text) 
    return response
    

def process_tests(response :str, test_name:str, ):
    data = response.json()
    for test in data:
        if(test["Name"] == test_name):
            uuid = test["UUID"]
            if (uuid):
                print("We found the target uuid {}".format(uuid))
                return uuid

def get_health():
    full_url = MES_URL + "/health"
    response = requests.get(
        full_url
    )
    print(response.status_code)
    print(response.text) 
    return response

    
if __name__ == "__main__":
    # post_test_stations()
    # get_test_stations()
    # response = get_tests("477D9F8A-01DD-4257-89AA-FDA02248CA52")
    # uuid = process_tests(response, "testgroup_flash_scb_local")
    response = post_tests("ba5f7541-7cd3-4259-8488-0971b429e85f", "OP40_Test", "OP40_Test")
    result = response.json()
    print(result)
    # get_health()