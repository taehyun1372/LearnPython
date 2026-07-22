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

if __name__ == "__main__":
    # Overall summary
    script_dir = Path(__file__).resolve().parent
    folder = Path.joinpath(script_dir, "repo")
    total_pass_count, total_fail_count = summary_test(folder)
    print(f"total pass : {total_pass_count}")
    print(f"total fail : {total_fail_count}")
    
    # Device summary
    script_dir = Path(__file__).resolve().parent
    folder = Path.joinpath(script_dir, "repo\\AT001CM")
    AT001CM_pass_count, AT001CM_fail_count = summary_test(folder)
    print(f"AT001CM pass : {AT001CM_pass_count}")
    print(f"AT001CM fail : {AT001CM_fail_count}")
    
    # Test summary
    script_dir = Path(__file__).resolve().parent
    folder = Path.joinpath(script_dir, "repo\\AT001CM\\test1.csv")
    AT001CM_test1_pass_count, AT001CM_test1_fail_count = summary_test(folder)
    print(f"AT001CM test1 pass : {AT001CM_test1_pass_count}")
    print(f"AT001CM test1 fail : {AT001CM_test1_fail_count}")