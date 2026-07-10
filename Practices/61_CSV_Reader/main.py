import csv
from datetime import datetime
import json, os
import requests
from threading import Lock

def process_test_result(report_path):
        with open(report_path, "r") as fd:
            gather = False
            now_iso = datetime.now().isoformat()
            start_time = now_iso
            end_time = now_iso
            case_execution = None
            case_executions = []
            for row in csv.reader(fd):
                if "Start_Time" in row and len(row) > 1:
                    dt = datetime.strptime(row[1], r"%Y-%m-%d %H:%M:%S")
                    start_time = dt.isoformat()
                if "End_Time" in row and len(row) > 1:
                    dt = datetime.strptime(row[1], r"%Y-%m-%d %H:%M:%S")
                    end_time = dt.isoformat()
                if "Test Case Title" in row:
                    gather = True
                elif gather and len(row) > 3 and row[2]: # case execution 
                    status = str(row[3]).strip().upper()
                    mes_status = "Not Executed"
                    if status in ["PASS", "PASSED"]:
                        mes_status = "Pass"
                    elif status in ["FAIL", "FAILED"]:
                        mes_status = "Fail"
                    elif status in ["SKIP", "SKIPPED"]:
                        mes_status = "Skipped"
                    case_execution = {
                            "Name": str(row[2]).strip(),
                            "StartTime": now_iso,
                            "EndTime": now_iso,
                            "TestStatus": mes_status,
                            "TestStepExecutions": [],
                        }
                    case_executions.append(case_execution)

                if gather and len(row) > 7 and case_execution != None: # step execution 
                    status = str(row[6]).strip().upper()
                    step_status = "Not Executed"
                    if status in ["PASS", "PASSED"]:
                        step_status = "Pass"
                    elif status in ["FAIL", "FAILED"]:
                        step_status = "Fail"
                    elif status in ["SKIP", "SKIPPED"]:
                        step_status = "Skipped"
                    case_execution["TestStepExecutions"].append({
                        "Name" : str(row[4]).strip(),
                        "StartTime": now_iso,
                        "EndTime": now_iso,
                        "TestStatus" : step_status,
                        "TestStepCmd" : str(row[5]).strip(),
                        "TestStepError" : str(row[7]).strip(),
                        "Metadata" : {}
                        })
        return case_executions, start_time, end_time
    
def post_result(result, start_time, end_time):
    full_url = "http://192.168.1.56:3003" + "/test-executions/"
    payload = {
        "TestUUID": "99910E83-F41A-40B5-8E88-55321AFC8E86",
        "TestPlanName": "THTEST0001",
        "ComponentSerial": "THABCD1234",
        "StartTime": start_time,
        "EndTime": end_time,
        "Metadata": {
            "overallResult": "Pass",
            "device": "",
            "testGroup": "",
            "reportPath": "",
        },
        "TestCaseExecutions": result,
    }
    response = requests.post(
        full_url,
        json=payload
    )
    print(response.status_code)
    print(response.text) 
    return response

class Database():
    """! The Database class.
    Defines the class that creates a database as a csv file. Stores key-value pair.
    This file can be accessed by anyone with the database object or the file location and name.
    NOTE This is not a peripheral.
    NOTE ok for IPC, but inefficient within the process.
    """
    
    def __init__(self, filepath):
        """! The initializer.
        @note This can be initialized during the beginning of any app. The app should push this database object across to different components of the app.
        @note Between processes, the filename is crucial to access the shared data.
        
        @param filepath     Full path of the file.
        @return  Instance of class.
        """
        super().__init__()
        self.__filepath = filepath
        self.__file_lock = Lock()
        # self.create_file()
    
    def read_db(self, key : str):
        """! Get Data from the database.
        @param  key     the key word to search the value.
        @return Value if found, else None.
        """
        try:
            with self.__file_lock:
                with open(self.__filepath,"r") as fd:
                    robj = csv.reader(fd)
                    for row in robj:
                        # Check if row is not blank
                        if row and row[0] == key:
                            # self.logger.info(f"Read {row[0]} :: {row[1]}")
                            return str(row[1])
                        
            raise Exception ('Key not found.')
        except Exception as ex:
            # self.logger.error(f"Read Failed. Exception: {str(ex)}")
            return None
        
    def write_db(self, key : str, value : str):
        """! Populate the database. Check and update if key already exists.
        @param  key     the key word to store the value with.
        @param  value   the value to be stored.
        @return True if update successful, else False.
        """
        try:
            with self.__file_lock:

                # Create file if it doesn't exist.
                temp_data = dict()
                if not os.path.exists(self.__filepath):
                    with open(self.__filepath, 'w'): pass
                else:                                   
                    # Read file and update temporary data dict.
                    with open(self.__filepath, 'r') as fd:
                        reader = csv.reader(fd)
                        for row in reader:
                            if len(row) == 2 and row[0]:
                                temp_data[row[0]] = row[1]
                      
                # Update the temporary data dict.
                temp_data[key] = value
                
                # Re-write the database again.
                with open(self.__filepath, 'w', newline='') as fd:            
                    writer = csv.writer(fd)
                    for k, v in temp_data.items():
                        writer.writerow([k, v]) if k else None
            
            # self.logger.info(f"UPDT. {key} :: {value}")
            return True
        except Exception as ex:
            # self.logger.error(f"Database Update Failed. Exception: {traceback.format_exc()}")
            return False
    
if __name__ == "__main__":
    # result, start_time, end_time = process_test_result("UAT_2026-04-22-16-13-12-TestReport.csv")
    # print(result)
    # post_result(result, start_time, end_time)
    # with open("result.json", "w", encoding="utf-8") as f:
    #     json.dump(result, f, indent=4)
        
    db = Database("UAT_2026-04-07-11-13-30-Database.csv")
    firmware = db.read_db("$DB_SCB_FW_VERSION")
    public_ky = db.read_db("$DB_SCB_SIGN_VERIFY_PUB_KEY")
    secondary_private_key = db.read_db("$DB_SECONDARY_SIGN_VERIFY_PRV_KEY")
    secondary_public_key = db.read_db("$DB_SECONDARY_SIGN_VERIFY_PUB_KEY")
    device_name = db.read_db("$DB_DEVICE_NAME")
    scb_component_id = db.read_db("$DB_SCB_COMPONENT_ID")
    ble_mac_addr = db.read_db("$DB_BLE_MAC_ADDR")
    print(firmware)
    print(public_ky)
    print(secondary_private_key)
    print(secondary_public_key)
    print(device_name)
    print(scb_component_id)
    print(ble_mac_addr)
    
    db.write_db("test_key1", "test_value1")
    db.write_db("test_key2", "test_value2")
    db.write_db("test_key3", "test_value3")
        