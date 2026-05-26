import asyncio
from bleak import BleakScanner, BleakClient

NAME = "Phone Alert Status"

async def scan():
    devices = await BleakScanner.discover()

    for d in devices:
        print(f"Name: {d.name}, Address: {d.address}")
        
        if d.name == NAME:
            async with BleakClient(d.address) as client:
                print("connected:", client.is_connected)
                
                for service in client.services:
                    print(f"[Service] {service.uuid}")
                    
                    for char in service.characteristics:
                        print(f"  [Characteristic] {char.uuid} | {char.properties}")
                        
                        
                        if "write" in char.properties:
                            await client.write_gatt_char(char.uuid, b"some data", response=False)
                            print(f"[Info] successfully wrote")
                            
                        if "read" in char.properties and not "notify" in char.properties :
                            try:
                                value = await client.read_gatt_char(char.uuid)
                                print(f"[Info] successfully read {char.uuid} -> {value}")
                            except Exception as e:
                                print(f"[Skip] {char.uuid} -> {e}")
                                    
            break             

if __name__ == "__main__":
    asyncio.run(scan())

