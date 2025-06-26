import clr
clr.AddReference("System")  # Needed to access .NET types
from System.Net import IPAddress

DEVICE_NAME = "Codesys_Control_Win_V3"
GATEWAY_NAME = "Gateway-6"
GATEWAY_IP_ADDRESS = "192.168.121.132"
GATEWAY_PORT = 1217
INSTANCE_IP_ADDRESS = "172.17.0.4"
INSTANCE_ID = "Instance1"
INSTANCE_PASSWORD = "Wonderous7641!"

proj = projects.primary

if proj is None:
    print("No project is currently opened!")
else:
        # Finds the object in the project, and return the first result
        devices = proj.find(DEVICE_NAME, True)
        if devices is not None:
            print(devices[0].get_name())
            device = devices[0]

            ip = IPAddress.Parse(INSTANCE_IP_ADDRESS)

            gateways = online.gateways
            matching_gateway = False
            gateway_names = []
            target_gateway_name = GATEWAY_NAME
            for gateway in gateways:
                gateway_names.append(gateway.name)
                if (gateway.config_params[0] == GATEWAY_IP_ADDRESS and  # Check ip address
                        gateway.config_params[1] == GATEWAY_PORT): # Check port
                    matching_gateway = True
                    target_gateway_name = gateway.name


            if not matching_gateway:
                print('No matching gateway found..creating a new gateway')

                params = {
                    0: GATEWAY_IP_ADDRESS,  # or use param.id == 0
                    1: GATEWAY_PORT  # or use param.id == 1
                }

                while(target_gateway_name in gateway_names):
                    prefix, suffix = target_gateway_name.split('-')
                    target_gateway_name = prefix + '-' + str(int(suffix) + 1)

                gateways.add_new_gateway(target_gateway_name, params)

            try:
                device.set_gateway_and_ip_address(target_gateway_name, ip)
                online_application = online.create_online_application()
                online_device = online_application.get_online_device()
                online.set_specific_credentials(target=online_device, username=INSTANCE_ID, password=INSTANCE_PASSWORD)
                online_device.connect()

                online_application.login(OnlineChangeOption.Try, True)
                online_application.start()
                # online_device.set_credentials_for_initial_user(username="Instance1", password="Wonderous7641!", can_change_password=True, must_change_password=False)
            except Exception as exception:
                print("Failed to set the target gateway ", target_gateway_name)













