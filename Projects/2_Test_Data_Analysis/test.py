import os
from pathlib import Path
from datetime import datetime
import pandas as pd
import csv

PATH1 = "C:\\Users\\ko1z528\\OneDrive - Kohler Co\\바탕 화면\\Code\\LearnPython\\Projects\\2_Test_Data_Analysis\\test_folder1"
PATH2 = "C:\\Users\\ko1z528\\OneDrive - Kohler Co\\바탕 화면\\Code\\LearnPython\\Projects\\2_Test_Data_Analysis"

SAMBA_OP00_ICP = "Y:\\TestFiles\\OP00\\ICP"
SAMBA_OP00_SCB = "Y:\\TestFiles\\OP00\\SCB"
SAMBA_OP20_SCB = "Y:\\TestFiles\\OP20\\SCB"
SAMBA_OP30_SCB = "Y:\\TestFiles\\OP30\\SCB"
SAMBA_OP30_DEVICE = "Y:\\TestFiles\\OP30\\Device"
SAMBA_OP40_BATTERY = "Y:\\TestFiles\\OP40\\Battery"
SAMBA_OP50_DEVICE = "Y:\\TestFiles\\OP50\\Device"
SAMBA_OP50_NFC = "Y:\\TestFiles\\OP50\\NFC"
SAMBA_OP60_DEVICE = "Y:\\TestFiles\\OP60\\Device"

START_DATE = "2026-07-01"
END_DATE = "2026-09-22"

def check_date_elapsed(path, date):
    folder = Path(path)
    folder_date = folder.stat().st_mtime
    folder_date = datetime.fromtimestamp(folder_date)
    input_date = datetime.strptime(date, "%Y-%m-%d")

    if folder_date > input_date:
        return True
    else:
        return False
    
def check_date_in_range(path, start_date, end_date):
    folder = Path(path)
    folder_date = folder.stat().st_mtime
    folder_date = datetime.fromtimestamp(folder_date)
    
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    if folder_date > start_date and folder_date < end_date:
        return True
    else:
        return False
    
def get_all_path_in_date_range(path, start_date, end_date):
    result = []
    path = Path(path)
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    with os.scandir(path) as entries:
        directories = sorted(
            (
                (entry, datetime.fromtimestamp(entry.stat().st_mtime))
                for entry in entries
                if entry.is_dir()
            ),
            key=lambda item: item[1],
        )

    for entry, modified_date in directories:
        if modified_date > end_date:
            break
        if modified_date >= start_date:
            file = Path(entry.path)
            # print(f"file name : {file.name}, modified date : {modified_date}")
            result.append(file)
    return result

def get_all_UAT_in_date_range(devices, start_date, end_date):
    result = []
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    for device in devices:
        device_name = device.name
        for UAT in device.iterdir():
            if isinstance(UAT, Path) and UAT.is_dir():
                test_name = UAT.name
                test_date_str = test_name.split('_')[1]
                test_date = datetime.strptime(test_date_str, "%Y-%m-%d-%H-%M-%S")
                if test_date >= start_date and test_date <= end_date:
                    # print(f"file name : {test_name}, test date : {test_date}")
                    result.append((UAT, device_name, test_date))
    return result
                    
def get_data_from_UAT(UAT: Path, device_name:str, test_date:datetime):
    test_data = None
    UAT_name = UAT.name
    failed = False
    last_pass_step = 0
    first_fail_step = 0
    passed_step_count = 0
    failed_step_count = 0
    skipped_step_count = 0
    total_step = 0
    for file in UAT.iterdir():
        if "TestReport.csv" in file.name:
            with open(file, newline='') as csvfile:
            # needs to be improved
                for _ in range(10):
                    next(csvfile)
                testrun = csv.DictReader(csvfile, delimiter=',')
                for step in testrun:
                    result = step.get("Test Step Status", None)
                    stepId = step.get("Test Step Id", None)
                    if result and stepId:
                        if result == "Pass":
                            passed_step_count += 1
                            last_pass_step = float(stepId)
                        elif result == "Fail":
                            failed_step_count += 1
                            if not failed:
                                first_fail_step = float(stepId)
                            failed = True
                        elif result == "Not Executed":
                            skipped_step_count += 1
                        total_step = float(stepId)
            if last_pass_step == total_step and not failed:
                # print(f"Test passed, {file.name}")
                pass
            test_data = {
                "device" : device_name,
                "UAT name" : UAT_name,
                "test date" : test_date,
                "passed" : not failed,
                "pass step count": passed_step_count,
                "fail step count" : failed_step_count,
                "skip step count" : skipped_step_count,
                "last pass step" : last_pass_step,
                "first fail step" : first_fail_step
            }
    return test_data

def find_specific_failure_from_dataframe(df:pd.DataFrame, step):
    return df.loc[df["first fail step"] == step]

def get_summary_from_dataframe(df:pd.DataFrame):
    device_summary = (
        df.groupby(["device", "passed"])
    .size()
    .unstack(fill_value=0)
    .rename(columns={True: "passed", False: "failed"})
    )
    # print(device_summary.to_string())
    
    test_summary = {
        "total test run" : len(df),
        "total pass test run" : int(df["passed"].eq(True).sum()),
        "total fail test run" : int(df["passed"].eq(False).sum()),
        "final pass device count" : int(device_summary["passed"].ge(1).sum()),
        "final fail device count" : int(device_summary["passed"].eq(0).sum()),
    }
    return pd.DataFrame([test_summary])

def get_test_summary(path, start_date, end_date):
    path = path
    all_devices = get_all_path_in_date_range(path, start_date, end_date)
    all_UATs = get_all_UAT_in_date_range(all_devices, start_date, end_date)
    test_result = [summary for UAT, device_name, test_date in all_UATs if (summary := get_data_from_UAT(UAT, device_name, test_date)) is not None]
    df = pd.DataFrame(test_result)
    print(df.head(100))
    summary = get_summary_from_dataframe(df)
    summary.insert(0, "path", path)
    print(summary.head())

    failure = find_specific_failure_from_dataframe(df, 5.5)
    print(failure.head(100))

if __name__ == "__main__":
    # result1 = check_date_elapsed(PATH1, START_DATE)
    # print(result1)
    
    # result2 = check_date_in_range(PATH1, START_DATE, END_DATE)
    # print(result2)
    
    # result3 = get_all_path_in_date_range(SAMBA_OP00_ICP, START_DATE, END_DATE)
    
    # result4 = get_all_UAT_in_date_range(result3, START_DATE, END_DATE)
    
    # result5 = [summary for UAT, device_name, test_date in result4 if (summary := get_data_from_UAT(UAT, device_name, test_date)) is not None]

    # df = pd.DataFrame(result5)
    # print(df.head(1000))

    # summary = get_summary_from_dataframe(df)
    # print(summary.head())
    
    # get_test_summary(SAMBA_OP00_ICP, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP00_SCB, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP20_SCB, START_DATE, END_DATE)
    get_test_summary(SAMBA_OP30_SCB, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP30_DEVICE, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP40_BATTERY, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP50_DEVICE, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP50_NFC, START_DATE, END_DATE)
    # get_test_summary(SAMBA_OP60_DEVICE, START_DATE, END_DATE)
    
    