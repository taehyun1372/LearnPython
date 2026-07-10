payload = {
    "EndTime" : "Today",
    "StartTime" : "Today",
    "Metadata" : {
        "overallResult" : "Pass",
        "device" : "SCB1234"
    }
}

result1 = payload.get("Metadata")
result2 = payload.get("Metadat2", "Not found")

print(result1)
print(result2)


result1["BleMAC"] = "AB:CD:EF"

optional_fields = {
    "NewItem1" : "NFC",
    "NewItem2" : "TOF",
    "NewItem3" : ""
}

for key, val in optional_fields.items():
    if val != "" : 
        result1[key] = val
        
        
print(payload)

print(result1)

