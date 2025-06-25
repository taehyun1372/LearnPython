import clr
clr.AddReference("System")  # Needed to access .NET types
from System.Net import IPAddress

DEVICE_NAME = "Codesys_Control_Win_V3"
GATEWAY_NAME = "Gateway-9"
IP_ADDRESS = "172.17.0.4"
TARGET_PORT = 1217

proj = projects.primary

if proj is None:
    print("No project is currently opened!")
else:
        # Finds the object in the project, and return the first result
        devices = proj.find(DEVICE_NAME, True)
        if devices is not None:
            print(devices[0].get_name())
            device = devices[0]

            ip = IPAddress.Parse(IP_ADDRESS)

            gateways = online.gateways
            matching_gateway = False
            for gateway in gateways:
                if gateway.name ==  GATEWAY_NAME:
                    matching_gateway = True

            if not matching_gateway:
                print('No matching gateway found..creating a new gateway')

                params = {
                    0: IP_ADDRESS,  # or use param.id == 0
                    1: TARGET_PORT  # or use param.id == 1
                }

                gateways.add_new_gateway(GATEWAY_NAME, params)

            try:
                device.set_gateway_and_ip_address(GATEWAY_NAME, ip)
            except Exception as exception:
                print("Failed to set the target gateway ", GATEWAY_NAME)













