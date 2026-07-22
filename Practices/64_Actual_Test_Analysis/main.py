import csv
from pathlib import Path
import os

def summary_test(repo_path : str):
    print(repo_path)
    if repo_path == None or repo_path == "": return None
    pass_count = 0
    fail_count = 0
    
    # file process
    if os.path.isfile(repo_path):
        with open(repo_path, newline='') as csvfile:
            testrun = csv.DictReader(csvfile, delimiter=',')
            for step in testrun:
                for key, value in step.items():
                    if key == "result":
                        if value == "Pass": pass_count += 1
                        elif value == "Fail": fail_count += 1
    else:
    # folder process
        for path in repo_path.rglob("*.csv*"):
            with open(path, newline='') as csvfile:
                testrun = csv.DictReader(csvfile, delimiter=',')
                for step in testrun:
                    for key, value in step.items():
                        if key == "result":
                            if value == "Pass": pass_count += 1
                            elif value == "Fail": fail_count += 1
    return pass_count, fail_count

def test_report_summary(report_folder_path):
    if os.path.isdir(report_folder_path):
        total_count = 0
        pass_count = 0
        fail_count = 0
        for path in report_folder_path.rglob("*TestReport.csv*"):
            with open(path, newline='') as csvfile:
                # needs to be improved
                for _ in range(10):
                    next(csvfile)
                testrun = csv.DictReader(csvfile, delimiter=',')
                for step in testrun:
                    result = step.get("Test Step Status", None)
                    if result :     
                        total_count += 1
                        if result == "Pass" : pass_count += 1
                        else : fail_count += 1
                        
        return total_count, pass_count, fail_count
    else:
        return None
    
def fail_step_summary(device_folder_path):
    result = []
    if os.path.isdir(device_folder_path):
        for report_folder_path in device_folder_path.rglob("*UAT*"):
            last_pass_step, first_fail_step = find_fail_step(report_folder_path)
            result.append({"path" : report_folder_path.name, "last_pass_step" : last_pass_step, "first_fail_step" : first_fail_step})
        return result
    else:
        return None
    
def find_fail_step(report_folder_path):
    if os.path.isdir(report_folder_path):
        last_pass_step = 0.0
        first_fail_step = 0.0
        for path in report_folder_path.rglob("*TestReport.csv*"):
            with open(path, newline='') as csvfile:
                # needs to be improved
                for _ in range(10):
                    next(csvfile)
                testrun = csv.DictReader(csvfile, delimiter=',')
                for step in testrun:
                    result = step.get("Test Step Status", None)
                    stepId = step.get("Test Step Id", None)
                    if result and stepId:
                        if result == "Pass":
                            last_pass_step = float(stepId)
                        else:
                            first_fail_step = float(stepId)
                            break
            break
        return last_pass_step, first_fail_step
    else:
        return None, None

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    folder1 = Path.joinpath(script_dir, "20260722_AT1091742228CM\\UAT_2026-07-22-09-41-24")
    total_count, pass_count, fail_count = test_report_summary(folder1)
    print(f"total : {total_count}, pass : {pass_count}, fail : {fail_count}")
    
    last_pass_step, first_fail_step = find_fail_step(folder1)
    print(f"last pass step : {last_pass_step}, first fail step : {first_fail_step}")
    
    folder2 = Path.joinpath(script_dir, "20260722_AT1091742228CM")
    fail_step_result = fail_step_summary(folder2)
    print("---Fail step summary---")
    print(fail_step_result)